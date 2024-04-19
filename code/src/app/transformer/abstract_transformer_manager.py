import re
from datetime import datetime
from src.core.transformer.transformer_manager_interface import ITransformerManager
from src.core.mapper.mapper_manager_interface import IMapperManager

class AbstractTransformerManager(ITransformerManager):

    def __init__(self, exclusions):
        self.mapper_manager = None
        self.exclusions = exclusions

    def set_mapper_manager(self, mapper_manager):
        if not isinstance(mapper_manager, IMapperManager):
            raise TypeError(f"The provided MapperManager does not implement the IMapperManager interface.")

        self.mapper_manager = mapper_manager

    def transform(self, data):
        self.is_initialized()

        return self.transform_data(data)

    def is_initialized(self):
        if self.mapper_manager is None:
            raise RuntimeError("No MapperManager defined.")

    def transform_data(self, data):
        """
        Transforms the data
        """
        transformed_data = []
        for record in data:
            transformed_record = self.transform_record(record)
            if self.has_exclusion(transformed_record):
                continue

            transformed_data.append(transformed_record)

        # Removes duplicates
        unique_records = list({frozenset(item.items()):item for item in transformed_data}.values())

        return unique_records

    def has_exclusion(self, record):
        for field_key in self.exclusions:
            if field_key not in record:
                continue

            exclusion = self.exclusions[field_key]
            field_value = exclusion["value"]
            operator = exclusion["operator"]
            if operator == "EQUALS":
                if  record[field_key] == field_value:
                    return True
            if operator == "DISTINCT":
                if record[field_key] != field_value:
                    return True

        return False

    def transform_record(self, record):
        """
        Transforms a record
        """
        mapper = self.mapper_manager.get()
        results = self.get_data_skeleton(mapper)

        for field_definition in mapper:
            value = self.transform_field(record, field_definition)
            results[field_definition["destination"]["field_name"]] = value

        return results

    def transform_field(self, record, field_definition):
        """
        Transforms a field
        """
        source = field_definition["source"]
        if not source["field_name"]:
            return ""

        destination = field_definition["destination"]
        field_name = source["field_name"]
        value = self.__resume_value(record, field_name)
        if not value:
            return destination["default_value"] if "default_value" in destination else ""

        field_type = source["type"]
        if field_type == "filter":
            value = self.__get_filtered_field_value(value, source["filter_definition"])
        else:
            value = self.__get_primitive_value(field_type, value)
            if value == "":
                return destination["default_value"] if "default_value" in destination else ""

        return value

    def __get_primitive_value(self, field_type, value):
        """
        Retrieves the primitive value of a field
        """
        if field_type == "date":
            try:
                value = self.__transform_epoch_to_formatted_date(value)
            except TypeError:
                return value
        elif field_type == "text":
            value = str(value)
        elif field_type == "boolean":
            value = bool(value)
        elif field_type == "special_fte":
            value = self.__transform_fte(value)
        elif field_type == "special_holiday_calendar":
            value = self.__transform_holiday_calendar_description(value)

        return value

    def get_data_skeleton(self, mapper):
        """
        Retrieves the data skeleton
        """
        data_skeleton = {}
        for item in mapper:
            destination = item["destination"]
            data_skeleton[item["destination"]["field_name"]] = ""

        return data_skeleton

    def __resume_value(self, record, field_name):
        """
        Resumes the value of an item, that might be a nested value or a plain value
        """
        if isinstance(field_name, list):
            return self.__get_nested_field_value(record, field_name)

        return record.get(field_name, "")

    def __get_nested_field_value(self, record, field_name):
        """
        Computes the value of a nested field
        """
        list_value = record.get(field_name[0], "")
        for key in field_name[1:]:
            try:
                list_value = list_value[key]
            except KeyError:
                list_value = ""
                break
            except TypeError:
                list_value = ""
                break
            except IndexError:
                list_value = ""
                break

        return list_value

    def __get_filtered_field_value(self, collection, filter_definition):
        """
        Retrieves the value of a filtered field
        """
        criteria = filter_definition["criteria"]
        for record in collection:
            filtered_value = record[criteria[0]] if criteria[0] in record else ""
            for key in criteria[1:]:
                try:
                    filtered_value = filtered_value[key]
                except KeyError as err:
                    filtered_value = ""
                    break
                except TypeError:
                    filtered_value = ""
                    break
                except IndexError:
                    filtered_value = ""
                    break

            if filter_definition["matching"] == "equals":
                if filter_definition["value"] == filtered_value:
                    return record[filter_definition["source_field"]]
            elif filter_definition["matching"] == "contains":
                if filter_definition["value"] in filtered_value:
                    return record[filter_definition["source_field"]]

        return ""

    def __transform_epoch_to_formatted_date(self, epoch_date):
        """
        Transforms miliseconds based epoch time to a Y-m-d date
        """
        if not epoch_date or epoch_date is None:
            return ""

        result = re.search(r'\d+', epoch_date)
        if not result:
            return ""

        timestamp = result.group(0)
        if not timestamp:
            return ""

        numeric_timestamp = int(int(timestamp) / 1000)

        return datetime.fromtimestamp(numeric_timestamp).strftime("%Y-%m-%d")

    def __transform_fte(self, fte):
        """
        Transforms the FTE to a percentage
        """
        return float(fte) * 100 if fte else ''

    def __transform_holiday_calendar_description(self, holiday_calendar_description):
        """
        Transforms the holiday calendar
        """
        pattern = re.compile(" ing calendar", re.IGNORECASE)
        holiday_calendar_description = pattern.sub(" Ingeniería", holiday_calendar_description)

        pattern = re.compile(" calendar", re.IGNORECASE)
        holiday_calendar_description = pattern.sub("", holiday_calendar_description)

        return holiday_calendar_description
