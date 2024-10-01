from datetime import datetime
from App.database import db

class Review(db.Model):
    __tablename__ = 'review'
    reviewID = db.Column(db.Integer, primary_key=True)
    studentID = db.Column(db.Integer, db.ForeignKey('student.studentID'), nullable=False)
    staffID = db.Column(db.Integer, db.ForeignKey('staff.staffID'), nullable=False)
    reviewType = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)  
    reviewDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())  # Auto set current date

    staff = db.relationship('Staff', backref='reviews')