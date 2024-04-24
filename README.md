# Cybertron: Transformation framework

Cybertron is a framework intended for retrieving data from one or several repositories, transforming it, and storing in output repositories.

For this purpose, pipelines are defined to manage the different stages of the process.

## Class model

Before we start, please take into account that this framework relies heavily on the interfaces defined in the core.
When creating new functionalities, you should implement these interfaces to make sure that the pieces are correctly aligned
and the classes exposes the expected methods.

## Project structure

There are three main folders:

- **app:** Contains the classes that model your application.
  - **input:** Contains the _input_ classes. These classes have to be created for each project.
  - **mapper:** Contains the _mapper_ classes. These classes have to be created for each project.
  - **transformer:** Contains the _transformer_ classes. These classes have to be created for each project.
  - **output:** Contains the _output_ classes. These classes have to be created for each project.
  - **orchestrator:** Contains the _orchestrator_ class. This class can be adapted for each project, but can be used as is.
- **core:** Contains the framework classes, that you should not modify.
  - **input:** Contains the _input_ interface.
  - **mapper:** Contains the _mapper_ interface.
  - **transformer:** Contains the _transformer_ interface.
  - **output:** Contains the _output_ interface.
  - **environment:** Contains the _environment_ service, which reads the environment variables and the configuration variables defined in the settings.yml file, and provides a common interface to manage them all.
  - **exception:** Contains generic exceptions.
  - **helper:** Contains generic services, such as a benchmark service and the logger.
  - **orchestrator:** Contains the _orchestrator_ interface, as well as abstract methods.
- **include:** Contains the connectors (i.e. BigQuery client, SuccessFactors client, SAP client, etc.).

## Process' stages

There are three different stages in the process:

1. **Input.** The data is queried from the input repository and stored in memory.
   Alternatively, the input data can be queried and processed record by record,
   but it requires modifying the default orchestrator (see the _Orchestrator_ section below).
2. **Transformation.** The data is transformed following rules defined in the mapper (see the _Mapper_ section below).
   These rules are coded in a special class that provides generic transformations out-of-the-box.
3. **Output.** The data is stored in the desired repository according to the structure defined in the mapper.

The workflow is modelled in the _Orchestrator_ class, that we will see in detail later.

## Modelling a new pipeline

A pipeline is the combination of the three stages that form a workflow, plus the mapper. In other words, an input, a mapper, a transformer, and an output.

To model a new pipeline, you have to follow these steps:

1. Include the classes in `app/app_manager.py`:

```
from src.app.mapper.global_mapper_manager import GlobalMapperManager

from src.app.input.global_input_manager import GlobalInputManager

from src.app.transformer.global_transformer_manager import GlobalTransformerManager

from src.app.output.global_output_manager import GlobalOutputManager
```

2. Inside the _run()_ method in the same file, initialize the orchestrator:

```
self.orchestrator.set_mapper_manager(GlobalMapperManager())

self.orchestrator.set_input_manager(GlobalInputManager())

self.orchestrator.set_transformer_manager(GlobalTransformerManager())

self.orchestrator.set_output_manager(GlobalOutputManager())
```

3. Optionally, you can define the mandatory environment variables at `environment_variables`.
   The variable names you set here will be checked. If not present, the application will halt.

4. Implement the input, mapper, transformer, and output classes to suit your needs. You will find demo classes that can guide you as an example.

## Orchestrator

The orchestrator is built-in to serve a default workflow that works as follows:

1. The input data is stored in memory.
2. The data is transformed and mapped.
3. The data is stored in the output repository.

This process is repeated for each pipeline sequentially.

What if you want to process record by record? Well, in this case you have to rewrite the orchestrator and prepare your pipeline classes to attend to this use case.
For example, instead of retrieving all the data, the input class should retrieve each record at a time. And the orchestrator would have a single iterator instead of three.

## Mapper

The mapper is a class that contains a JSON structure that defines how the input data matches the output data:

```
  DATA_MAPPER = [
      {
          "destination": {
              "field_name": "person_id",
              "type": "STRING",
          },
          "source": {
              "field_name": ["employmentNav", "personNav", "personId"],
              "type": "text",
          },
      },
      {
          "destination": {
              "field_name": "email_address",
              "type": "STRING",
          },
          "source": {
              "field_name": ["employmentNav", "personNav", "emailNav", "results"],
              "type": "filter",
              "filter_definition": {
                  "criteria": ["__metadata", "uri"],
                  "matching": "contains",
                  "value": "emailType='4049'",
                  "source_field": "emailAddress",
              },
          },
      },
      {
          "destination": {
              "field_name": "global_effective_start_date",
              "type": "STRING",
          },
          "source": {
              "field_name": "startDate",
              "type": "date",
          },
      },
  ]
```

The _source_ type matches what you define at `app/transformer/abstract_transform_mananger.py`:

```
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
```

Of course, you can redefine this method to suit your needs because it is part of the application.

When you have a nested structure, you can point it like this: `"field_name": ["employmentNav", "personNav", "emailNav", "results"]`

## Entry points

There are one entry point that you can rewrite to adapt to your requirements:
1. `web.py`: A Flask application that runs the application after the execution of an endpoint.

# How to develop
## Execute project in local
After clone project, just run:

`$ make run`

### Open the localhost

`http://127.0.0.1:5000/version`

### Open Swagger UI
`http://127.0.0.1:5000/swagger/`


# Add new dependencies to the project
## Add the new dependency with poetry
```bash
$ poetry add Flask
```

## Update the requirements.txt
Use the `make freeze-dependencies` command instead `pip freeze`.
