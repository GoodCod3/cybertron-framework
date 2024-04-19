import os
import time
from google.cloud import bigquery
from google.api_core.exceptions import NotFound, BadRequest
from src.core.helper.logger import Logger
from src.core.exception.abort_process_exception import AbortProcessException
from google.api_core.retry import Retry

class BigQueryConnector:
    """
    Handles the communication with BigQuery
    """

    def __init__(self, project, dataset, insert_attempts, sleep_interval):
        self.project = project
        self.dataset = dataset
        self.insert_attempts = insert_attempts
        self.sleep_interval = sleep_interval
        self.client = bigquery.Client()
        self.logger = Logger()

    def __wait_for_job(self, query_job):
        retry = Retry()
        retry(query_job.result)

    def __create_table(self, table_name, schema):
        """
        Creates a table in BigQuery
        """
        dataset_ref = bigquery.DatasetReference(self.project, self.dataset)
        table_ref = dataset_ref.table(table_name)
        table = bigquery.Table(table_ref, schema=schema)

        return self.client.create_table(table)

    def __get_or_create_table(self, table_name, schema):
        """
        Retrieves an existing table from BigQuery, or creates it if it does not exist
        """
        dataset_ref = bigquery.DatasetReference(self.project, self.dataset)
        table_ref = dataset_ref.table(table_name)

        try:
            table = self.client.get_table(table_ref)
        except BadRequest:
            table = self.__create_table(table_name, schema)
        except NotFound:
            table = self.__create_table(table_name, schema)

        return table

    def __exists(self, table_name, key_field, value):
        """
        Checks whether a value exists
        """
        query_string = f"SELECT * FROM {self.dataset}.{table_name} WHERE {key_field} = '{value}'"
        query_job = self.client.query(query_string)
        self.__wait_for_job(query_job)

        return query_job.result().total_rows

    def __row_to_dict(self, row):
        """
        Converts a row in a dictionary (all strings)
        """
        dictionary = dict(row)
        for key in dictionary.keys():
            dictionary[key] = str(dictionary[key])

        return dictionary

    def __get_field_type(self, field_name, schema):
        """
        Retrieves the field type
        """
        for field in schema:
            if field_name == field.name:
                return field.field_type

    def initialize_table(self, table, schema):
        """
        Initializes a table
        """
        self.__get_or_create_table(table, schema)

    def drop_table(self, table_name):
        """
        Drops a table if exists
        """
        statement = f"DROP TABLE IF EXISTS {self.dataset}.{table_name}"
        query_job = self.client.query(statement)
        self.__wait_for_job(query_job)

        return query_job.result()

    def copy_table(self, source_table, destination_table, schema):
        """
        Copies one table's contents to another
        """
        destination_table_id = f"{self.project}.{self.dataset}.{destination_table}"
        self.drop_table(destination_table)
        job_config = bigquery.QueryJobConfig(destination=destination_table_id)
        query_string = f"SELECT * FROM {self.dataset}.{source_table}"
        query_job = self.client.query(query_string, job_config=job_config)
        self.__wait_for_job(query_job)

        return query_job.result()

    def truncate_table(self, table_name, schema):
        """
        Truncates a table
        """
        table = self.__get_or_create_table(table_name, schema)
        statement = f"TRUNCATE TABLE {self.dataset}.{table_name}"
        query_job = self.client.query(statement)
        self.__wait_for_job(query_job)

        return query_job.result()

    def insert_or_update(self, data, key_field, table_name, schema):
        """
        Inserts or updates records (comparison by key_field)
        """
        # Prepares the new records to be inserted
        ids = []
        records_to_insert = []
        for item in data:
            ids.append(item[key_field])
            records_to_insert.append(item)

        # Gets the non-matching records from the database
        dataset = self.get_results(table_name)
        for record in dataset:
            if not record.get(key_field) in ids:
                records_to_insert.insert(0, self.__row_to_dict(record))

        if len(records_to_insert) == 0:
            return False

        # Inserts the new records
        self.truncate_table(table_name, schema)
        self.logger.info(f"Trying to insert {len(records_to_insert)} rows")
        self.insert_data(records_to_insert, table_name, schema, False)

        return True

    def get_dataset(self):
        """
        Gets the dataset
        """

        return self.dataset

    def execute_query(self, query_string):
        """
        Performs a query and returns the results
        """

        query_job = self.client.query(query_string)
        self.__wait_for_job(query_job)

        return query_job.result()

    def get_results(self, table_name):
        """
        Returns all the results of the given table
        """

        return self.execute_query(f"SELECT * FROM {self.dataset}.{table_name}")

    def insert_data(self, data, table_name, schema, table_must_be_empty = True):
        """
        Inserts data into a BigQuery table
        """
        result = None
        attempts = 0
        total_attempts = 15
        while result == None and attempts < self.insert_attempts:
            try:
                if table_must_be_empty:
                    total = self.get_row_count(table_name)
                    if total:
                        raise NotFound(f"The table {table_name} still have records")

                table = self.__get_or_create_table(table_name, schema)
                errors = self.client.insert_rows_json(table, data)
                if errors == []:
                    print("New rows have been added.")
                    result = True
                else:
                    print("Encountered errors while inserting rows: {}".format(errors))
                    result = False

            except NotFound as err:
                self.logger.warning(f"BigQuery cannot insert records: attempt {attempts + 1}/{total_attempts}", True)
                attempts = attempts + 1
                time.sleep(self.sleep_interval)
                continue

        if result == None:
            raise AbortProcessException(500, "Los datos no se han podido insertar en BigQuery por indisponibilidad de la plataforma")
        elif result == False:
            raise AbortProcessException(500, "Los datos no se han podido insertar en BigQuery: {}".format(errors))

        return True

    def update_data(self, data, key_field, table_name, schema):
        """
        Updates data in a BigQuery table
        """
        keys = data.keys()
        values = data.values()
        statement = f"UPDATE `{self.project}.{self.dataset}.{table_name}` SET "
        for key, value in data.items():
            if self.__get_field_type(key, schema) == "STRING":
                statement += "%s = '%s'," %(key, value)
            else:
                statement += "%s = %s," %(key, int(value))

        statement = statement[:-1] + f" WHERE {key_field}='{data[key_field]}'"
        query_job = self.client.query(statement)

        return query_job.result()

    def get_row_count(self, table_name):
        """
        Gets the row count of a table
        """
        return self.get_results(table_name).total_rows
