# Falcon Case

# Requirements
The task is to implement a data processing pipeline in the cloud. Set up a running environment aligned with the technologies mentioned below:

- :heavy_check_mark: A Readme file containing information you deem useful for someone getting to know your code and want to try the system out
- :heavy_check_mark: Develop the application in Python 3
- :x: A REST endpoint is taking a dummy JSON input, and the server puts the REST payload on Redis or another tool you think is well suited for the task
- :x: A Consumer is running in the application, taking the freshly received message and persists it in a database of your choice
- :heavy_check_mark: A REST endpoint is implemented for retrieving all the messages persisted in JSON format from the database
- :x: The message should also be pushed through Websockets for listening browser clients at the time the message was received on the REST endpoint
- :x: A simple HTML page is implemented to show the real time message delivery
- :heavy_check_mark: Please setup a github repository to host the code and share it with your final note for review

We're looking for that:

- :x: All tasks are solved in the solution
- :x: The application has a solid commit history
- :x: The application is built with scalability and maintainability in mind
- :x: The application is built for testability, demonstrated by actual tests
- :x: Your solution reflects a sense of quality you would be confident in releasing to production
- :x: Documentation is applied to code / repository describing intent and purpose, as well as complicated / non obvious choices in the implementation