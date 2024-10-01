from App.database import db

class Staff(db.Model):
    __tablename__ = 'staff'
    staffID = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)


