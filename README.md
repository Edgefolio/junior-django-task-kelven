# Fund-View
Django coding exercise to enable upload and view of examples of funds

# TASKS

| Task  | Sub-Task | Status | Notes |
|-------|----------|--------|-------|
| Generate a simple django application with simply SQLite as the database | N/A (Overarching goal) | In Progress | -- |
|Single Model called 'Fund' representaing data in the sample file | | In Progress ||
|A way to import CSV file matching the sample provided, via a file upload form on a Django web page | | Not Started | Data will initially be keyed via fixtures with a view to replace once upload form built |
|Build web page displaying:| list of funds available in the database as a table with one column per field on the Fund model| Not Started ||
|Build web page displaying:| a dropdown at the top of the page, allowing to select a Strategy value, and filtering the funds displayed in the page by one of the available Strategy choices| Not Started ||
|Build web page displaying:| total number of Funds in the database (at the bottom of the table)| Not Started ||
|Build web page displaying:| if the current page is filtered by a Strategy value, then this number should be the number of Fund objects matching the filter| Not Started ||
|Build web page displaying:| at the bottom of the table, display one number that is the sum of all Fund AUM values (AUM is one number field listed in the sample CSV file)| Not Started ||
|A REST API endpoint that can:| list Fund objects that are in the database, in a JSON format| Not Started ||
|A REST API endpoint that can:| a way to filter the objects by the Strategy field, by appending a query parameter ?strategy=[value] to the URL of that endpoint| Not Started ||
|A REST API endpoint that can:| another endpoint to view a JSON representation of a single Fund object identified by its id field| Not Started ||
| Testing | write one or more automated tests within the django app, checking that some of the specs above are working. Tests can be run with the command manage.py test | Not Started | |


# BUGS

| Bug | Brief Details | Status | Notes |
|-----|---------------|--------|-------|
| 403 Error - DjangoAdmin | Initial attempts to access django admin were prevented as gitpod enviornment was not recognised as trusted origin | RESOLVED | django v4 implemented changes to trusted origins which required gitpod env to be added as 'CSRF_TRUSTED_ORIGINS' in settings.py - per django docs https://docs.djangoproject.com/en/4.0/releases/4.0/#csrf-trusted-origins-changes-4-0 |

