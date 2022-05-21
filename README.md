# Colourdle

A daily colour code breaker game.

A siple flask app where the user must try to guess the colour code in less than 8 tries.

### Architechture

## Getting Started

Activate the python virtual environment:
`$ source venv/bin/activate` (or '' $ venv\Scripts\activate' on Windows)

To run the app:
`$flask run`

To stop the app:
`$^C`

To exit the environment:
`$deactivate`

### Prerequisites

Requires python3 (https://www.python.org/download/releases/3.0/), flask, venv, and sqlite

```
pip3 install flask
python3 -m venv venv
$ pip install flask

```

### Installing

Install python3, sqlite3

1. Set up a virtual environment:

- use pip or another package manager to install virtualenv package `pip install virtualenv`
- start the provided virtual environment
  `source virtual-environment/bin/activate`
- This should include flask and all the required packages

2. Install sqlite

- [Windows instructions](http://www.sqlitetutorial.net/download-install-sqlite/)
- In \*nix, `sudo apt-get install sqlite`

3. Build the database: `flask db init`
4. `flask run`

This should start the app running on localhost at port 5000, i.e. [http://localhost:5000/index](http://localhost:5000/index)

## Running the tests

A few tests now:

To run unit tests
`python -m tests.unittest`

To run selenium tests, make sure that you have the
appropriate web driver installed. In this case it should be geckodriver for Firefox,
and it assumes that it is installed in the test directory.
Then start the webserver in TestingConfig, and run
`python -m tests.systemtest`

## Deployment

via localhost

## Built With

vim and git

## Authors

- **Ben Willcocks (22260513) & Zeina Zabaneh (10476052)**

## Git Logs

## Acknowledgments

- Built following CITS5505 Workshops and Labs as well as the [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by **Miguel Grinberg**.
