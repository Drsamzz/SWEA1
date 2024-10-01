from App.database import db

class Student(db.Model):
    __tablename__ = 'student'
    studentID = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    degree = db.Column(db.String(50), nullable=False)

    reviews = db.relationship('Review', backref='student', lazy=True)
