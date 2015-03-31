# Appython library

The library has the following components:

* `components/api` contains helpers to build an easy to use API with Flask-RESTful. It has a base `Exception`, a decorator to provide authentication, an enum with status codes, a base class for all endpoints, and a collection of common fields, requests, and response objects.

* `components/cron` provides a base class for cron endpoints.

* `components/models` has a base class for all NDB models with a few commonly used fields.

* `components/queue` provides a base class for tasks endpoints and a base class to manage the coding and decoding of data, and launching tasks.

* `components/sentry` integrates [Sentry](https://getsentry.com) with the different pieces of the project (the Flask app, the API, cron tasks, and queue).

* `components/user` has some utils for user management (email cleaning, password management and generation, API key generation) as well as a standard callback for Flask-Login to load an user model from NDB.

* `utils` is an assorted collection of functions used by all apps.

Read the source code comments for more information, and the check out the samples folder for real world uses.
