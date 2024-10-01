from App.models import Student, Staff, Review
from App.database import db

def create_staff(first_name, last_name, role):
    staff = Staff(firstName=first_name, lastName=last_name, role=role)
    db.session.add(staff)
    db.session.commit()
    print(f'Staff {first_name} {last_name} created!')

def list_staff():
    staff_members = Staff.query.all()
    for staff in staff_members:
        print(f'{staff.staffID}: {staff.firstName} {staff.lastName}, Role: {staff.role}')
