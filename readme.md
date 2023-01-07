# Simple framework

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
Framework close to Flask: was made for fun and for deeper understanding what is going on "under the hood".
Can manage as static routes as dynamic routes. 
	
## Technologies
Project is created with:
* gunicorn 20.1.0
* parse 1.19.0
* WebOb 1.8.7
* Postman
	
## Setup
To run this project:

```
$ git pull https://github.com/alexa-kobrynets/fun-simple_framework
$ pip install -r requirements
$ gunicorn app:app
```