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