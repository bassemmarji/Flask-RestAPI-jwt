# Flask-RestAPI-jwt
A Flask Rest API with user authentication taking into consideration the updates of Flask-JWT-Extended version 4.1

Introduction:

A RESTAPI with Flask using Token based authentication.

Technologies:

Flask
Flask-RESTFUL-0.3.8 
Flask-JWT_Extended-4.1.0
Flask-SQLAlchemy-2.4.4

General Info:

JWT stands for JSON WEB TOKEN, is a secure way of transferring random tokens between two parties or entities.
API (application programming interface) allows communication between two applications to retrieve or submit the data.
REST API falls under the request-response category.
Flask is a micro-framework used by python developers to build rest API.

Pre-requisites: 
 requirements.txt
  Flask
  Flask-RESTFUL-0.3.8 
  Flask-JWT_Extended-4.1.0
  Flask-SQLAlchemy-2.4.4
  PyJWT-2.0.1
  
Scope of functionalities:
    API endpoints:
      User registration
      User Login
      Query registered users.
      Delete registered users.
      Add a New Author
      Query Authors
      Delete An/All Author
      Revoke Access Token
      Reinstate Access Token
      Revoke Refresh Token

Screenshots using Postman utility:

Registering a new user:

![image](https://user-images.githubusercontent.com/74184047/114380940-47adc380-9b93-11eb-87e2-4951cd7e1a04.png)

Login:

![image](https://user-images.githubusercontent.com/74184047/114380996-53998580-9b93-11eb-8fb6-d94359abb92d.png)

  {
    "message": "Logged in as test",
    "access_token":  "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxODIyMDY2MiwianRpIjoiMWJiYmYxYTYtOGYxNC00ODIxLTgxZWMtZDFjMWQ5MTMzMDVjIiwibmJmIjoxNjE4MjIwNjYyLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoidGVzdCIsImV4cCI6MTYxODIyMTU2Mn0.YObK4qb4ZpSxQDQjIoP6f4dD1Qez30LTvsxocOxF3s8",
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxODIyMDY2MiwianRpIjoiZTBiN2Q2ZWMtNTUyMi00NWQ1LTkzNjYtMDZlZTBkYjI1NzQ0IiwibmJmIjoxNjE4MjIwNjYyLCJ0eXBlIjoicmVmcmVzaCIsInN1YiI6InRlc3QiLCJleHAiOjE2MjA4MTI2NjJ9.Lh7LmIEgUsRWcpOm3RhtYf7pvHKc6LL3WxFLiQ6wFB8"
  }
  
Querying users:

![image](https://user-images.githubusercontent.com/74184047/114381221-8b083200-9b93-11eb-85a6-006d203dfe11.png)


Add a new author:

![image](https://user-images.githubusercontent.com/74184047/114381253-96f3f400-9b93-11eb-9a12-938d04b50695.png)

![image](https://user-images.githubusercontent.com/74184047/114381285-9e1b0200-9b93-11eb-9851-d429a814d3d0.png)

Query Authors:

![image](https://user-images.githubusercontent.com/74184047/114381320-aa06c400-9b93-11eb-9d68-3504db4078ae.png)

Delete Author:

![image](https://user-images.githubusercontent.com/74184047/114381378-ba1ea380-9b93-11eb-9b52-1f3f6ba0d26b.png)

![image](https://user-images.githubusercontent.com/74184047/114381399-c0148480-9b93-11eb-8fa4-6dfa1452763b.png)

Delete Users:

![image](https://user-images.githubusercontent.com/74184047/114381438-cb67b000-9b93-11eb-9185-dc320d1bd19e.png)

Revoke Access Token:

![image](https://user-images.githubusercontent.com/74184047/114381484-d7ec0880-9b93-11eb-8fa3-6ff9249f6a2b.png)

Reinstate Access Token using the Refresh Token:

![image](https://user-images.githubusercontent.com/74184047/114381540-e508f780-9b93-11eb-8ad3-4ad53b19bcb1.png)

Revoke Refresh Token:

![image](https://user-images.githubusercontent.com/74184047/114381582-f3efaa00-9b93-11eb-9ec3-4042ed025ee7.png)












