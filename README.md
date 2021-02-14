# The Pine Digital Growth Python Package

This package contains a variety of miscellaneous Python helper/utility functions used across different Pine Digital 
projects.

## Installation

Install using [pip](https://pypi.org/project/pppine/) with:

```
pip install pppine
```

## Components

### Python Helpers

Tired of searching StackOverflow for answers to the most basic of Python problems? We've got you covered. 

While these helpers may seem random in nature, they've come in handy hundreds of times across multiple Pine Digital 
products. They're solutions with a personal spin, some with more of a creative touch than others.

#### Random Generators

* Generate a string of random numbers of length `n`.
* Extract initials out of a person's or organization's name.
* Create a temporary password that's easier to look at than UUID's.
* Generate short UUID's. Based on [shortuuid](https://pypi.org/project/shortuuid/), but even shorter.

#### Date, Time, and DateTime Helpers

* Get the current date and time, but in your local timezone.
* Greet your users with the proper time of the day. Is it the 'morning', 'afternoon', or 'evening'? Plug in a time 
  object to find out.
* Get today's date and time, but set the time to midnight.
* Convert a date object to a datetime object.
* Parse a datetime from a string or number. Perfect when working with JSON and API's.

#### Address & Contact Info Helpers

* Capitalize all the right things in an address the way .title() can't.
* Format a mailing address nicely, whether you want it in one line or many.
* Clean an address inputted from a form.
* Properly capitalize people's names that start with 'Mc', 'Mac', 'de ', and so on.
* Format a phone number properly based on an inputted country.
* Check whether an inputted string is an email address.

#### General Helpers

* Replace a string's character at a specified index without all the extra work.
* Check whether a file is a certain file type. You never know, file extensions might not always tell a true story.
    * While you're at it, raise a specialized exception if a certain file isn't the file type you want it to be.
* Get the class name of an object.
* Check whether a string actually represents a list.
* Turn a list, dictionary, or any other Python literal into a JSON string, but encode it in base64.
* Take that base64-converted JSON string and convert it back into a Python literal.
* Ever see some strings that should be a list? Turn those into an actual list.
  
### Django Helpers

### Encoders

* Get the ultimate encoder for JSON dumps. Very Django-friendly. (COMING SOON)

### Miscellaneous

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
