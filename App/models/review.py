from App.database import db

class Review(db.Model):
    __tablename__ = 'review'
    reviewID = db.Column(db.Integer, primary_key=True)
    studentID = db.Column(db.Integer, db.ForeignKey('student.studentID'), nullable=False)
    staffID = db.Column(db.Integer, db.ForeignKey('staff.staffID'), nullable=False)
    reviewType = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=True)

    student = db.relationship('Student', back_populates='reviews')
    staff = db.relationship('Staff', back_populates='reviews')
