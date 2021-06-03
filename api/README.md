# Pokerena API

Poker games&results management, built with Flask REST API with PostgreSQL database

## Motivation

With the start of the pandemic and less social gatherings, a group of friends had the idea to play online poker plus video chat as a way to keep in touch. This piece of software track the games and results.

## Prerequisites

- Python >= 3.7

## Installing

It's recommended that you create a virtual environment, I'm using here `venv` that comes bundled with python

```
$ python -m venv venv
$ source venv/bin/activate
```

Now install the dependencies

```
$ python -m pip install -r requirements.txt
```

All set, you can run the Flask development server

```
$ flask run
```

To check the API docs visit http://localhost:5000/apidocs

## Running the tests

```
$ python -m pytest
```

## Deployment

Add additional notes to deploy this on a live system
