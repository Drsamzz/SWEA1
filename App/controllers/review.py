from App.models import staff
from App.database import db

def review_student(self, review):
        db.session.add(review)
        db.session.commit()

def view_student_reviews(self, student):
    return student.reviews

def delete_review(self, review):
    db.session.delete(review)
    db.session.commit()

def edit_review(self, review, new_data):
    for key, value in new_data.items():
        setattr(review, key, value)
    db.session.commit()