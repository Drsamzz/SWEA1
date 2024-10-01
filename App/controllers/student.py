from App.models import staff
from App.database import db

 def add_student(self, student):
        db.session.add(student)
        db.session.commit()

def edit_student_details(self, student, new_data):
    # assuming new_data is a dict with the updated fields
    for key, value in new_data.items():
        setattr(student, key, value)
    db.session.commit()

def delete_student(self, student):
    db.session.delete(student)
    db.session.commit()

def search_student(self, student_id):
    return Student.query.get(student_id)