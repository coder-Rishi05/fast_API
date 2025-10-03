### 🚀 FastAPI Basics – Easy Hinglish Guide

FastAPI ek modern web framework hai Python ke liye, jo super fast, easy to use, aur production ready hai.Fast Api with python + Project.


Endpoints : 

GET
POST
PUT
DELETE

Basics

from fastapi import FastAPI

app = FastAPI()


student = {
    1:{
        "name":"rishi",
        "age" : 18,
        "class":"BCA-III"
    },
    2:{
        "name":"rishi",
        "age" : 18,
        "class":"BCA-III"
    },
    3:{
        "name":"rishi",
        "age" : 118,
        "class":"BCA-III"
    },
    4:{
        "name":"rishi",
        "age" : 18,
        "class":"BCA-III"
    }
}

@app.get('/')
def index():
    return {"name":"first name"} 


@app.get('/st/{st_id}') # here we are passing dynamic value of st_id
def get_st(st_id: int): # defining dynamic variable it should be same data type as of the student object key.
    return student[st_id] # passing the dynamic variable

# GET : return info
# POST : create something new
# PUT : update
# Delete : delete


Command to start python serevr using uvicorn

 syntax       fileName:the app is variable which having FastApi() --reload to start the server
 ex:                 uvicorn python:app --reload
