from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel 

app = FastAPI()


student = {
    1:{
        "name":"kri",
        "age" : 28,
        "class":"BCA-III"
    },
    2:{
        "name":"rishi",
        "age" : 18,
        "class":"BCA-III"
    },
    3:{
        "name":"mili",
        "age" : 118,
        "class":"BCA-III"
    },
    4:{
        "name":"nok",
        "age" : 18,
        "class":"BCA-III"
    }
}


St_info = {
    1:{
        "name":"jhon",
        "age":"19",
        "year":"year 12"
    }
}

students = {
    1: {"name": "kri", "age": 28, "year": "BCA-III"},
    2: {"name": "rishi", "age": 18, "year": "BCA-III"}
}

class Student(BaseModel):
    name:str
    age:int
    year:str





@app.get('/')
def index():
    return {"name":"first name"} 


@app.get('/st/{st_id}') # here we are passing dynamic value of st_id
async def get_st(st_id: int = Path( description="The id of this studnet yiu want to see ", gt=0, lt=10)): # defining dynamic variable it should be same data type as of the student object key.
    return student[st_id] # passing the dynamic variable


@app.get('/get-by-name')
def get_student(name : Optional[str] = None ):
    for student_id in student:
        if student[student_id]["name"] == name:
            return student[student_id]
        return {"Data not found"}



@app.get('/getQuery')
def get_std(*,name : Optional[str] = None, age : int ): # multiple query parameter
    for student_id in student:
        if student[student_id]["name"] == name:
            return student[student_id]
        return {"Data not found"}
# gt, lt, 

# GET : return info
# POST : create something new
# PUT : update
# Delete : delete

# combination of query and path parameter.

@app.get('/getname/{st_id}')
def get_stdId(*, st_id : int ,test : int,name : Optional[str] = None ):
    for student_id in student:
        if student[st_id]["name"] == name:
            return student[st_id]
        return {"Data not found"}
    

### Request body and post method.


@app.post("/create-student/{std_id}")
def create_std(std_id: int, student: Student):
    if std_id in students:
        return {"error": "Student already exists"}
    
    students[std_id] = student.model_dump()  # ✅ use model_dump() instead of dict()
    return students[std_id]

