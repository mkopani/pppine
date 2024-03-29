# Changelog

v1.3.2 (2021-08-25)

* General fixes
* Changed author email

v1.3.1 (2021-03-24)
-----------------

* More fixes to import statements

v1.3 (2021-03-06)
-----------------

* Add query string parameters to a URL with `add_url_params()` in `urls`.

v1.2 (2021-02-21)
-----------------

* Added a middleware component for Django projects.
    * Have Django automatically store an authenticated user's timezone (as saved in their profile) 
        in the current session variables.

v1.1.1 (2021-02-20)
-------------------

* Addressed import issues

v1.1 (2021-02-20)
-------------------

* NEW: Avoid running into problems when converting your data to JSON strings by using our universalized version of the comprehensive DjangoJSONEncoder.
* Also added a date-safe encoder that converts dates to integers for front-end parsing.
* Fixed importlib import statement to properly detect whether Django is installed.

v1.0.4 (2021-02-18)
-------------------

* NEW: Get a comprehensive list of a model's field names by calling get_field_names() from the Django component.
* Updates to README

v1.0.3 (2021-02-17)
-------------------

* Addressed import errors

v1.0.2 (2021-02-13)
-------------------

* Corrections to README
* Moved CHANGELOG to main directory

v1.0.1 (2021-02-13)
-------------------

* Shuffled files and directories
* Complete overhaul of README
* Added CHANGELOG

v1.0 (2021-02-12)
-----------------

* Initial upload
