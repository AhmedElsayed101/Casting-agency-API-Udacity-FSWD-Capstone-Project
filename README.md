# Casting agency of Udacity

This project is my last project of full stack web development nano-degree, it was epic as  I tried to finish this nano degree in less than 20 days although the estimated time for it is 4 months, it's a  demo for a casting agency where you can find actors and movies and directors.

All backend code follows [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/). 

<hr/>

## Getting Started

### Project hierarchy

### Pre-requisites and Local Development 

Developers using this project should already have Python3, pip and postgresql installed on their local machines.

From the base directory run 
```
pip install requirements.txt
```
. All required packages are included in the requirements file. 

You have to create a new postgresql database using 
```
createdb capstone
```
You have to check for the `setup.sh` file to make sure that DATABASE_URL matches with your system

To run the application run the following commands: 
```
python manage.py db migrate
python manage.py db upgrade

python manage.py runserver
```
congratulations, server is running on (http://127.0.0.1:5000/)

<hr/>

### Tests
In order to run tests navigate to the base dicrectory and run the following commands: 

```
dropdb capstone_test
createdb capstone_test

python test_api.py
```
<hr/>

## API Reference

### Getting Started
- Base URL:  This app can only be run locally on (http://127.0.0.1:5000/) 
  It is  hosted as a base URL on (https://capstone102.herokuapp.com/)
- Authentication: This version of the application requires authentication, you can login using (https://capstone102.herokuapp.com/login) or (http://127.0.0.1:5000/login) which will redirects you to the auth0 third party authentication to login, you can retreive your token from the url.
There are 3 token in the `setup.sh` file which represent the 3 rules of our app. they may have expired by the time you are cloning this repo.

<hr/>

### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
The API will return three error types when requests fail:
- 400: Bad Request
- 404: Resource Not Found
- 422: Not Processable 

<hr/>

### Endpoints 

### **GET**  '/api/actors'
#### - Retreive all actors

##### Payload
``` json
None
```

##### Headers
``` json
{
    "Authorization":"Bearer <assistant token at least>"
}
```
##### Success Response
``` json

{
    "actors": [
        {
            "age": 30,
            "gender": "male",
            "id": 1,
            "name": "mohamed"
        },
        {
            "age": 20,
            "gender": "female",
            "id": 2,
            "name": "noha"
        },
        {
            "age": 11,
            "gender": "male",
            "id": 3,
            "name": "mohamed"
        },
        {
            "age": 6,
            "gender": "male",
            "id": 4,
            "name": "ahmed"
        }
    ],
    "actors_number": 4,
    "success": true
}

```
<hr/>

### **POST**  '/api/actors'
#### - Create a new actor

##### Payload
``` json
{
	"name": "name example",
	"age" : 30,
    "gender": "male"
}
```

##### Headers
``` json
{
    "Authorization":"Bearer <director token at least>"
}
```
##### Success Response
``` json
{
    "created": 5,
    "success": true
}
```
<hr/>

### **GET**  '/api/actors/<int:5>'
#### - Retreive an actor

##### Payload
``` json
None
```

##### Headers
``` json
{
    "Authorization":"Bearer <assistant token at least>"
}
```
##### Success Response
``` json
{
    "actor": {
        "age": 123132,
        "gender": ";skdafk;sdf",
        "id": 5,
        "name": "mohamed"
    },
    "success": true
}
```

<hr/>

### **DELETE**  '/api/actors/<int:5>'
#### - Delete an actor

##### Payload
``` json
None
```

##### Headers
``` json
{
    "Authorization":"Bearer <director token at least>"
}
```
##### Success Response
``` json
{
    "deleted": 5,
    "success": true
}
```
<hr/>

### **PATCH**  '/api/actors/<int:2>'
#### - Edit an actor

##### Payload
``` json
{
	"name": "name example",
	"age" : 30,
    "gender": "male"
}
```

##### Headers
``` json
{
    "Authorization":"Bearer <assistant token at least>"
}
```
##### Success Response
``` json
{
    "success": true,
    "updated": 2
}
```
<hr/>

### **GET**  '/api/movies'
#### - Retreive all movies

##### Payload
``` json
None
```

##### Headers
``` json
{
    "Authorization":"Bearer <assistant token at least>"
}
```
##### Success Response
``` json
{
    "movies": [
        {
            "id": 1,
            "start_time": "Sun, 01 Nov 2015 00:00:00 GMT",
            "title": "new moSFASFDvie"
        },
        {
            "id": 2,
            "start_time": "Sun, 01 Nov 2015 00:00:00 GMT",
            "title": "new moSFASFDvie"
        },
        {
            "id": 3,
            "start_time": "Sun, 01 Nov 2015 00:00:00 GMT",
            "title": "new moSFASFDvie"
        },
        {
            "id": 4,
            "start_time": "Sun, 01 Nov 2015 00:00:00 GMT",
            "title": "new moSFASFDvie"
        }
    ],
    "movies_number": 4,
    "success": true
}

```
<hr/>

### **POST**  '/api/movies'
#### - Create a new movie

##### Payload
``` json
{
	"title": "new movie",
	"start_time": "2015-11-1"
}
```

##### Headers
``` json
{
    "Authorization":"Bearer <producer token at least>"
}
```
##### Success Response
``` json
{
    "created": 10,
    "success": true
}
```
<hr/>

### **GET**  '/api/movies/<int:5>'
#### - Retreive a movie

##### Payload
``` json
None
```

##### Headers
``` json
{
    "Authorization":"Bearer <assistant token at least>"
}
```
##### Success Response
``` json
{
    "movie": {
        "id": 5,
        "start_time": "Sun, 01 Nov 2015 00:00:00 GMT",
        "title": "new moSFASFDvie"
    },
    "success": true
}
```

<hr/>

### **DELETE**  '/api/actors/<int:5>'
#### - Delete an actor

##### Payload
``` json
None
```

##### Headers
``` json
{
    "Authorization":"Bearer <producer token at least>"
}
```
##### Success Response
``` json
{
    "deleted": 5,
    "success": true
}
```
<hr/>


### **PATCH**  '/api/movies'
#### - Edit a  movie

##### Payload
``` json
{
	"title": "new movie",
	"start_time": "2015-11-1"
}
```

##### Headers
``` json
{
    "Authorization":"Bearer <director token at least>"
}
```
##### Success Response
``` json
{
    "success": true,
    "updated": 6
}
```
<hr/>



