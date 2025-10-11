# ===========================================================
# 📘 FASTAPI STUDENT MANAGEMENT PROJECT
# ===========================================================

from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# -----------------------------------------------------------
# 🧾 Dummy Data — Predefined Students
# -----------------------------------------------------------

student = {
    1: {"name": "kri", "age": 28, "class": "BCA-III"},
    2: {"name": "rishi", "age": 18, "class": "BCA-III"},
    3: {"name": "mili", "age": 118, "class": "BCA-III"},
    4: {"name": "nok", "age": 18, "class": "BCA-III"},
}

students = {
    1: {"name": "kri", "age": 28, "year": "BCA-III"},
    2: {"name": "rishi", "age": 18, "year": "BCA-III"},
}

# -----------------------------------------------------------
# 🧠 Pydantic Models — Data Validation & Structure
# -----------------------------------------------------------

class Student(BaseModel):
    name: str
    age: int
    year: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


# ===========================================================
# ✅ ACTIVE ROUTES (Clean + Corrected)
# ===========================================================

@app.get("/")
def index():
    return {"message": "Welcome to the Student Management API!"}


# 🧩 Create Student (POST)
@app.post("/create-student/{std_id}")
def create_std(std_id: int, student: Student):
    if std_id in students:
        return {"error": "Student already exists"}
    students[std_id] = student.model_dump()   # Converts Pydantic model to dict
    return {"success": True, "data": students[std_id]}


# ✏️ Update Student (PUT)
@app.put("/update-std/{std_id}")
def update_student(std_id: int, student: UpdateStudent):
    if std_id not in students:
        return {"error": "Student not found"}

    # Access the student record and update fields if provided
    if student.name is not None:
        students[std_id]["name"] = student.name
    if student.age is not None:
        students[std_id]["age"] = student.age
    if student.year is not None:
        students[std_id]["year"] = student.year

    return {"success": True, "updated_data": students[std_id]}


# 🔍 Get Student by ID (GET)
@app.get("/get-student/{std_id}")
def get_student(std_id: int = Path(description="The ID of the student you want to retrieve", gt=0, lt=10)):
    if std_id not in students:
        return {"error": "Student not found"}
    return students[std_id]


# 🔎 Get Student by Query (name and age)
@app.get("/get-query/")
def get_student_by_query(name: Optional[str] = None, age: Optional[int] = None):
    for student_id, details in students.items():
        if (name and details["name"] == name) or (age and details["age"] == age):
            return details
    return {"error": "No matching student found"}


# ===========================================================
# 🧩 OLD ROUTES (Commented for reference)
# ===========================================================

"""
@app.get('/st/{st_id}')
async def get_st(st_id: int = Path(description="The id of this student you want to see", gt=0, lt=10)):
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
