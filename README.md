# Falcon Case

## Requirements
The task is to implement a data processing pipeline in the cloud. Set up a running environment aligned with the technologies mentioned below:

- :heavy_check_mark: A Readme file containing information you deem useful for someone getting to know your code and want to try the system out.
- :heavy_check_mark: Develop the application in Python 3.
- :heavy_check_mark: A REST endpoint is taking a dummy JSON input, and the server puts the REST payload on Redis or another tool you think is well suited for the task.
- :heavy_check_mark: A Consumer is running in the application, taking the freshly received message and persists it in a database of your choice.
- :heavy_check_mark: A REST endpoint is implemented for retrieving all the messages persisted in JSON format from the database.
- :x: The message should also be pushed through Websockets for listening browser clients at the time the message was received on the REST endpoint
- :x: A simple HTML page is implemented to show the real time message delivery
- :heavy_check_mark: Please setup a github repository to host the code and share it with your final note for review

## We're looking for that:

- :x: All tasks are solved in the solution
- :x: The application has a solid commit history
- :x: The application is built with scalability and maintainability in mind
- :x: The application is built for testability, demonstrated by actual tests
- :x: Your solution reflects a sense of quality you would be confident in releasing to production
- :x: Documentation is applied to code / repository describing intent and purpose, as well as complicated / non obvious choices in the implementation

## How To Use
There are two options for running the application.

### Option 1 - Running it straight.
The first option is to run the application locally on a workstation that has all the python packages required, see `requirements.txt` for the packages.
Option 1 has primarily been used for development and testing, and as such does not use the same stack as option 2. Specifically, the stack does not include redis or postgresql, instead it uses simple caching and sqlite.

To get started, ensure that you have python3.6 installed, and execute the following commands:

- `pip install -r requirements.txt`
- `cd app`
- `python main.py`

This will start a simple debugging web server hosting the API. The url for the server is `http://127.0.0.1/api` which contains Swagger documentation for the endpoints that were implemented.

### Option 2 - Run it through docker-compose
The second option is to run the application using `docker-compose`. This is the preferred option, as it uses the intended stack.

To get started, ensure that you have docker installed, and execute the following commands:

- `docker-compose build`
- `docker-compose up`

This will create the docker images, and the different docker containers that are then started to host the API. The url for the server is `http://127.0.0.1/api` which contains Swagger documentation for the endpoints that were implemented.

To give you a more complete picture of what docker images are used for the application, they are as follows:

- `tiangolo/uwsgi-nginx-flask:python3.6` - python3.6 is the development language that the API was implemented in, and the image provides a web server through `nginx` and an application server through `uwsgi`.
- `redis:alpine` - redis is used as an in-memory cache for the data requested over the API.
- `postgres:alpine` - postgres is used to persist the JSON objects on a database.
- `adminer` - adminer is used to provide an administrative overview of the postgres database.
