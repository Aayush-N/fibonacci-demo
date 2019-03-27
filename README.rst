Fibonacci Demo
============

Finds the Nth term of Fibonacci sequence

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Introduction
------------

This is a Python/Django application that will display the Nth number in
Fibonacci sequence. For instance, if N is 6 and the sequence starts with
[1,1..] then it should display ‘8’ as the 6th element in the sequence.

It also prints out the time taken to compute this answer.

Also supports complete user management - Sign In/Sign Up, etc.


Method of execution:

-  Get the Nth term value from user.
-  Check if the corresponding value for Nth term already exists in DB,
   if it does, use it. This elimates the need to compute the value every
   time even for the same numbers. **Improving performance
   considerably.**
-  If not, compute the value for the input and store it in DB for future
   reference.
-  Redirect to answer page and display Value as well as Time Taken.

--------------

API Implementation
~~~~~~~~~~~~~~~~~~

API exists at the url: `/api/v1/fibonacci/`_. This accepts the POST JSON
and gives the value and time taken as reponse.

.. _/api/v1/fibonacci/: /api/v1/fibonacci/