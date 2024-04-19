from google.cloud import bigquery
from src.core.output.output_manager_interface import IOutputManager
from src.core.mapper.mapper_manager_interface import IMapperManager
from src.include.bigquery_connector import BigQueryConnector
from src.core.exception.no_data_to_process_exception import NoDataToProcessException

class AbstractOutputManager(IOutputManager):

    def __init__(self):
        self.insert_attempts = 25
        self.sleep_interval = 3
        self.mapper_manager = None

    def set_mapper_manager(self, mapper_manager):
        if not isinstance(mapper_manager, IMapperManager):
            raise TypeError(f"The provided MapperManager does not implement the IMapperManager interface.")

        self.mapper_manager = mapper_manager

    def put(self, data):
        self.__is_initialized()

        self.table_schema = self.__build_table_schema()
        self.bigquery_connector = BigQueryConnector(self.project, self.dataset, self.insert_attempts, self.sleep_interval)
        self.bigquery_connector.drop_table(self.table_name)
        self.bigquery_connector.initialize_table(self.table_name, self.table_schema)
        self.__insert_data(data)

    def __is_initialized(self):
        if self.mapper_manager is None:
            raise RuntimeError("No MapperManager defined.")

    def __build_table_schema(self):
        mapper = self.mapper_manager.get_flattened()
        schema = []
        for item in mapper:
            destination = item["destination"]
            nullable = destination["nullable"] if "nullable" in destination else "NULLABLE"
            default_value = destination["default_value"] if "default_value" in destination else None
            schema.append(bigquery.SchemaField(destination["field_name"], destination["type"], nullable, default_value))

        return schema

    def __insert_data(self, data):
        if len(data) == 0:
            raise NoDataToProcessException()

        if len(data) <= 1000:
            self.bigquery_connector.insert_data(data, self.table_name, self.table_schema, True)
        else:
            chunks = list(self.__split_data(data, 1000))
            for chunk in chunks:
                self.bigquery_connector.insert_data(chunk, self.table_name, self.table_schema, False)

    def __split_data(self, data, chunk_size):
        for i in range(0, len(data), chunk_size):
            yield data[i:i + chunk_size]
