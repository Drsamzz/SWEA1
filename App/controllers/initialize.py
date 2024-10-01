from .user import create_user
from .staff import create_staff
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    create_staff('Jon', 'Nancoo', 'Lecturer')
