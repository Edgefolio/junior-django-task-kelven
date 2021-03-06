# Fund-View
Django coding exercise to enable upload and view of examples of funds

# TASKS

| Task  | Sub-Task | Status | Notes |
|-------|----------|--------|-------|
| Generate a simple django application with simply SQLite as the database | N/A (Overarching goal) | COMPLETED | -- |
|Single Model called 'Fund' representaing data in the sample file | N/A | COMPLETED | |
|A way to import CSV file matching the sample provided, via a file upload form on a Django web page | | INCOMPLETE | Unresolved bug with csv file upload |
|Build web page displaying:| list of funds available in the database as a table with one column per field on the Fund model| COMPLETED | |
|Build web page displaying:| a dropdown at the top of the page, allowing to select a Strategy value, and filtering the funds displayed in the page by one of the available Strategy choices| COMPLETED | Incorporates django-filter |
|Build web page displaying:| total number of Funds in the database (at the bottom of the table)| COMPLETED ||
|Build web page displaying:| if the current page is filtered by a Strategy value, then this number should be the number of Fund objects matching the filter| COMPLETED ||
|Build web page displaying:| at the bottom of the table, display one number that is the sum of all Fund AUM values (AUM is one number field listed in the sample CSV file)| COMPLETED ||
|A REST API endpoint that can:| list Fund objects that are in the database, in a JSON format| COMPLETED | Incorporates rest_framework |
|A REST API endpoint that can:| a way to filter the objects by the Strategy field, by appending a query parameter ?strategy=[value] to the URL of that endpoint| COMPLETED |  |
|A REST API endpoint that can:| another endpoint to view a JSON representation of a single Fund object identified by its id field| COMPLETED | Accessed via fund name in fund table |
| Testing | write one or more automated tests within the django app, checking that some of the specs above are working. Tests can be run with the command manage.py test | COMPLETED | Small number of basic tests performed |


# BUGS

| Bug | Brief Details | Status | Notes |
|-----|---------------|--------|-------|
| File Upload | File upload results in Type Error | UNRESOLVED | Unresolved TypeError |

