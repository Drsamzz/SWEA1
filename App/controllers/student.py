from App.models import Student, Staff, Review
from App.database import db

def create_student(first_name, last_name, degree):
    student = Student(firstName=first_name, lastName=last_name, degree=degree)
    db.session.add(student)
    db.session.commit()
    print(f'Student {first_name} {last_name} created!')

def list_students():
    students = Student.query.all()
    for student in students:
        print(f'{student.studentID}: Name: {student.firstName} {student.lastName}, Degree: {student.degree}')

def get_student(student_id):
    student = Student.query.get(student_id)
    if student:
        print(f'ID: {student.studentID}, Name: {student.firstName} {student.lastName} has been found.')
    else:
        print("Student not found.")

def edit_student(student_id, first_name, last_name, degree):
    student = Student.query.get(student_id)
    if student:
        student.firstName = first_name
        student.lastName = last_name
        student.degree = degree
        db.session.commit()
        print(f'Student {student_id} updated.')
    else:
        print("Student not found.")

def delete_student(student_id):
    student = Student.query.get(student_id)
    if student:
        db.session.delete(student)
        db.session.commit()
        print(f'Student {student_id} deleted.')
    else:
        print("Student not found.")