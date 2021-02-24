# The Pine Digital Growth Python Package

This package contains a variety of miscellaneous Python helper/utility functions used across different Pine Digital 
projects.

## Installation

Install using [pip](https://pypi.org/project/pppine/) with:

```
pip install pppine
```

## What's In The Box?

### Python Helpers

Tired of searching StackOverflow for answers to the most basic of Python problems? We've got you covered. 

While these helpers may seem random in nature, they've come in handy hundreds of times across multiple Pine Digital 
products. They're solutions with a personal spin, some with more of a creative touch than others.

#### Random Generators

* Generate a string of random numbers of length `n`.
* Extract initials out of a person's or organization's name.
* Create a temporary password that's easier to look at than UUID's.
* Generate short UUID's. Based on [shortuuid](https://pypi.org/project/shortuuid/), but even shorter.

(*Import from `pppine.python.generators`*)

#### Date, Time, and DateTime Helpers

* Get the current date and time, but in your local timezone.
* Greet your users with the proper time of the day. Is it the 'morning', 'afternoon', or 'evening'? Plug in a time 
  object to find out.
* Get today's date and time, but set the time to midnight.
* Convert a date object to a datetime object.
* Parse a datetime from a string or number. Perfect when working with JSON and API's.

(*Import from `pppine.python.datetime`*)

#### Address & Contact Info Helpers

* Capitalize all the right things in an address the way .title() can't.
* Format a mailing address nicely, whether you want it in one line or many.
* Clean an address inputted from a form.
* Properly capitalize people's names that start with 'Mc', 'Mac', 'de ', and so on.
* Format a phone number properly based on an inputted country.
* Check whether an inputted string is an email address.

(*Import from `pppine.python.contact`*)

#### General Helpers

* Replace a string's character at a specified index without all the extra work.
* Check whether a file is a certain file type. You never know, file extensions might not always tell a true story.
    * While you're at it, raise a specialized exception if a certain file isn't the file type you want it to be.
* Get the class name of an object.
* Check whether a string actually represents a list.
* Turn a list, dictionary, or any other Python literal into a JSON string, but encode it in base64.
* Take that base64-converted JSON string and convert it back into a Python literal.
* Ever see some strings that should be a list? Turn those into an actual list.

(*Import from `pppine.python.general`*)
  
### Django Helpers

Make your day-to-day Django tasks easier with these helpers and shorthand notations.

* Get a comprehensive list of a model's field names.
* Raise a 404 if one or several URL slugs are nonempty.
* Get the verbose name of a model instance's field.
* Shorthand notation to check whether a Django object/query exists.
* Shorthand notation to return a queried object or `None` if not found.
* Reverse a URL namespace with query strings while writing the cleanest code. No f-strings or `%s` required on your end.
* Fetch the URL of the page you were redirected from.
* Update a model instance by dictionary rather than field by field.
* Convert a Django QueryDict (e.g. `request.GET`) to a regular dictionary.
* Safely update an object from another model instance with similar field names.

(*Import from `pppine.django`*)

### Encoders

* Get the ultimate encoder for JSON dumps. Very Django-friendly.


### Middleware

* Have Django automatically store an authenticated user's timezone (as saved in their profile) 
  in the current session variables

### Miscellaneous

This is more of a data file than a set of helpers, yet still helpful when working with forms that involve countries, 
provinces, and states.

* Get a list of tuples for
  * Countries
  * Canadian Provinces
  * US States
  
e.g.

```
[
  ('AB', 'Alberta'),
  ('BC', 'British Columbia'),
  ('SK', 'Saskatchewan'),
  ('MB', 'Manitoba'),
  ('ON', 'Ontario'),
  ('QC', 'Quebec'),
  ('NB', 'New Brunswick'),
  ('NS', 'Nova Scotia'),
  ('PE', 'Prince Edward Island'),
  ('NL', 'Newfoundland and Labrador'),
  ('YT', 'Yukon'),
  ('NT', 'Northwest Territories'),
  ('NU', 'Nunavut')
]
```

(*Import from `pppine.misc`*)
