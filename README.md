# Colourdle

A daily colour code breaker game.

A simple flask app where the user must try to guess the colour code in less than 8 tries.

### Architechture
-HTML-
1. Registration page - register.html, the user will create a username and the username is passed to the GameUser database
2. Login page - login.html, the user logs in using their created username 
3. Game page - index.html, the game page with the user's username displayed

-CSS-
1. Styling for all three html pages - style.css

-JS-
1. Javascript for all three html pages - script.js

-PY-
1. Application factory and Python package identifiaction for directory - __init__.py
2. Python shell for databases - colourdle.py
3. Python config classes - config.py
4. Flask forms to retrieve user input - forms.py
5. Defining the databases - models.py
6. Python code handling exchange of data between html, javascript and python - routes.py
7. Unit tests - test.py

-DB-
1. File containing the two databases - app.db, the databases contained are Game which stores the users scores, date score was obtained, and the username of the user and GameUser which stores the user's username and information related to the user

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

## Authors

- **Ben Willcocks (22260513) & Zeina Zabaneh (10476052)**

## Git Logs

## Acknowledgments

- Built following CITS5505 Workshops and Labs as well as the [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by **Miguel Grinberg**.
- Micheal Bauer question solution referenced at https://stackoverflow.com/questions/59975596/connect-javascript-to-python-script-with-flask
- user9501250 question solution referenced at https://stackoverflow.com/questions/2894946/passing-javascript-variable-to-python
