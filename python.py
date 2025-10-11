from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# ------------------------------------------------------------
# 🎓 Example data sets (separate for clarity)
# ------------------------------------------------------------

# For basic student info (used in /st and /get routes)
student = {
    1: {"name": "kri", "age": 28, "class": "BCA-III"},
    2: {"name": "rishi", "age": 18, "class": "BCA-III"},
    3: {"name": "mili", "age": 21, "class": "BCA-II"},
    4: {"name": "nok", "age": 19, "class": "BCA-I"}
}

# For another dataset (different purpose)
St_info = {
    1: {"name": "john", "age": 19, "year": "Year 12"}
}

# For CRUD operations (main database for POST & PUT)
students = {
    1: {"name": "kri", "age": 28, "year": "BCA-III"},
    2: {"name": "rishi", "age": 18, "year": "BCA-II"}
}


# ------------------------------------------------------------
# 🧩 Pydantic Models
# ------------------------------------------------------------

class Student(BaseModel):
    name: str
    age: int
    year: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


# ------------------------------------------------------------
# 💤 Commented old routes (just for reference)
# ------------------------------------------------------------

"""

@app.get('/')
def index():
    return {"name": "first name"}

@app.get('/st/{st_id}')
async def get_st(st_id: int = Path(description="ID of student", gt=0, lt=10)):
    return student[st_id]

@app.get('/get-by-name')
def get_student(name: Optional[str] = None):
    for student_id in student:
        if student[student_id]["name"] == name:
            return student[student_id]
    return {"Data not found"}

@app.get('/getQuery')
def get_std(*, name: Optional[str] = None, age: int):
    for student_id in student:
        if student[student_id]["name"] == name:
            return student[student_id]
    return {"Data not found"}

@app.get('/getname/{st_id}')
def get_stdId(*, st_id: int, test: int, name: Optional[str] = None):
    for student_id in student:
        if student[st_id]["name"] == name:
            return student[st_id]
    return {"Data not found"}
"""


# ------------------------------------------------------------
# 🚀 ACTIVE ROUTES (Clean CRUD)
# ------------------------------------------------------------

# 🟩 CREATE Student
@app.post("/create-student/{std_id}")
def create_std(std_id: int, student: Student):
    if std_id in students:
        return {"error": "Student already exists"}

    students[std_id] = student.model_dump()
    return {"message": "Student created successfully!", "data": students[std_id]}


# get data


@app.get('/')
def index():
    return {"name": "first name"}

# get by id
@app.get("/get-student/{std_id}")
def get_student(std_id: int = Path(description="Enter the student ID you want to fetch")):
    if std_id not in students:
        return {"error": "Student not found"}
    return {"data": students[std_id]}

# 🟨 UPDATE Student
@app.put("/update-student/{std_id}")
def update_student(std_id: int, student: UpdateStudent):
    if std_id not in students:
        return {"error": "Student does not exist"}

    # Fetch existing record
    existing_student = students[std_id]

    # Update only provided fields
    if student.name is not None:
        existing_student["name"] = student.name
    if student.age is not None:
        existing_student["age"] = student.age
    if student.year is not None:
        existing_student["year"] = student.year

    # Save back
    students[std_id] = existing_student
    return {"message": "Student updated successfully!", "data": existing_student}


# 🟦 GET All Students (for checking)
@app.get("/get-students")
def get_all_students():
    return students
