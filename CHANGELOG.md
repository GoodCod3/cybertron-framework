# Finance data changelog

This file reflects the changes of the *Finance data* project.

## Version `0.0.1`

- First version of the project.
- Main skeleton implemented with major improvements on the data mapping area.

## Version `1.0.0`

- Full refactor using the new ETL architecture.

## Version `1.1.0`

- Main refactor for expanding the employee record attending to the subrecords (personal information, employee information...).
- Some new fields added.

## Version `1.1.1`

- Disables the basic auth.
- Converts the trigger URL to GET.

## Version `1.2.0`

- Refactors the Orchestrator to allow several input managers.
- Refactors the TransformerManager to process three new data sources.

## Version `1.2.1`

- Improves the logic to match the desired output.
- Optimizes the overall process to make it much more efficient (+90% faster).
- Reworks the mapper to make it easier and more flexible.

## Version `1.2.2`

- Maps the Position entity fields, plus new employee fields (person_id and assignment_id_external).

## Version `1.2.3`

- In case an employee has no personal data associated, it is retrieved from the previous state of this employee.

## Version `1.3.0`

- New strategy: instead of merging the data, we will feed separate tables for each entity.

## Version `1.3.1`

- Implements a new fields group: Work Order.

## Version `1.3.2`

- Implements new fields and a special mechanism for excluding records.

## Version `1.3.3`

- Fixes the position_owner field, which was empty.

## Version `1.3.4`

- Updates some mapping.
- Implements an exclusion mechanism that allows filtering records by entity.

## Version `1.3.5`

- Implements the Payment entity.

## Version `1.3.6`

- Adds the effective end date to the Payment entity.

## Version `1.3.7`

- Adds new fields to some entities: Global (New Cost Center and Is Contingent Worker), Position (Job Title), Payment (Bank Country code, BIC, Currency code).

## Version `1.4.0`

- Implements a new pipeline for the country of the employee.

## Version `1.5.0`

- Refactors the Environment service to make it compatible with configuration files, and transforms it in a singleton.
- Updates the Global and the Position mapping services.

## Version `1.5.1`

- Removes the authentication because it is not necessary anymore.

## Version `1.5.2`

- Adds a new field from the Position entity: cust_clientFocus.

## Version `1.5.3`

- Adds a missing field from the Global entity: costCenterNav.name.

## Version `1.5.4`

- Fixes the SSFF URL to add the costCenterNav.name field.

## Version `1.6.0`

- Implements a new pipeline to store employees coming from SAP.

## Version `1.7.0`

- Implements two new pipelines to store absences data.
