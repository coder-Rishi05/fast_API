from fastapi import FastAPI, Path

app = FastAPI()


student = {
    1:{
        "name":"rishi",
        "age" : 28,
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
async def get_st(st_id: int = Path( description="The id of this studnet yiu want to see ", gt=0, lt=10)): # defining dynamic variable it should be same data type as of the student object key.
    return student[st_id] # passing the dynamic variable


@app.get('/get-by-name')
def get_student(name : str ):
    for student_id in student:
        if student[student_id]["name"] == name:
            return student[student_id]
        return {"Data not found"}
# gt, lt, 

# GET : return info
# POST : create something new
# PUT : update
# Delete : delete