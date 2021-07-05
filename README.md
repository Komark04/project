Explanation:
To run the API use python 3.9 (I used PyCharm) you will need to export the libraries pandas, flask, time and json.
To run the application, use the flask command you will need to tell your terminal the application to work with by exporting the FLASK_APP environment variable:
Type in terminal: (I used git bash)

$ export FLASK_APP=assignment
$ flask run

Where assignment is the file name. after that on your local machine enter the Ip you got and test the API for example: 127.0.0.1:5000/sessionId/27820661-9082-4c93-8961-336423fc46c9 where 27820661-9082-4c93-8961-336423fc46c9 is the session id.
