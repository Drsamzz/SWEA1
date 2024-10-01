import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User, Student, Staff, Review
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize )


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)




# Student CLI commands

@app.cli.command("create-student", help="Creates a new student")
@click.argument("first_name")
@click.argument("last_name")
@click.argument("degree")
def create_student_command(first_name, last_name, degree):
    student = Student(firstName=first_name, lastName=last_name, degree=degree)
    db.session.add(student)
    db.session.commit()
    print(f'Student {first_name} {last_name} created!')

@app.cli.command("list-students", help="Lists all students")
def list_students_command():
    students = Student.query.all()
    for student in students:
        print(f'{student.studentID}: {student.firstName} {student.lastName}, Degree: {student.degree}')

@app.cli.command("get-student", help="Get a student by ID")
@click.argument("student_id")
def get_student_command(student_id):
    student = Student.query.get(student_id)
    if student:
        print(f'Student {student.firstName} {student.lastName} found.')
    else:
        print("Student not found.")

@app.cli.command("student-edit", help="Edits a student's details")
@click.argument("student_id")
@click.argument("first_name")
@click.argument("last_name")
@click.argument("degree")
def edit_student_command(student_id, first_name, last_name, degree):
    student = Student.query.get(student_id)
    if student:
        student.firstName = first_name
        student.lastName = last_name
        student.degree = degree
        db.session.commit()
        print(f'Student {student_id} updated.')
    else:
        print("Student not found.")

@app.cli.command("delete-student", help="Deletes a student by ID")
@click.argument("student_id")
def delete_student_command(student_id):
    student = Student.query.get(student_id)
    if student:
        db.session.delete(student)
        db.session.commit()
        print(f'Student {student_id} deleted.')
    else:
        print("Student not found.")



# Staff CLI commands

@app.cli.command("create-staff", help="Creates a new staff member")
@click.argument("first_name")
@click.argument("last_name")
@click.argument("role")
def create_staff_command(first_name, last_name, role):
    staff = Staff(firstName=first_name, lastName=last_name, role=role)
    db.session.add(staff)
    db.session.commit()
    print(f'Staff member {first_name} {last_name} created!')

@app.cli.command("staff-list", help="Lists all staff members")
def list_staff_command():
    staff_members = Staff.query.all()
    for staff in staff_members:
        print(f'{staff.staffID}: {staff.firstName} {staff.lastName}, Role: {staff.role}')



# Review CLI commands

@app.cli.command("review-create", help="Creates a new review")
@click.argument("student_id")
@click.argument("staff_id")
@click.argument("review_type")
@click.argument("description")
def create_review_command(student_id, staff_id, review_type, description):
    student = Student.query.get(student_id)
    staff = Staff.query.get(staff_id)
    if student and staff:
        review = Review(studentID=student_id, staffID=staff_id, reviewType=review_type, description=description)
        db.session.add(review)
        db.session.commit()
        print(f'Review for student {student_id} by staff {staff_id} created.')
    else:
        print("Student or staff not found.")

@app.cli.command("review-list", help="Lists all reviews for a student")
@click.argument("student_id")
def list_reviews_command(student_id):
    student = Student.query.get(student_id)
    if student:
        reviews = student.reviews
        for review in reviews:
            print(f'Review {review.reviewID}: {review.reviewType}, {review.description}')
    else:
        print("Student not found.")

@app.cli.command("review-edit", help="Edits a review")
@click.argument("review_id")
@click.argument("review_type")
@click.argument("description")
def edit_review_command(review_id, review_type, description):
    review = Review.query.get(review_id)
    if review:
        review.reviewType = review_type
        review.description = description
        db.session.commit()
        print(f'Review {review_id} updated.')
    else:
        print("Review not found.")

@app.cli.command("review-delete", help="Deletes a review by ID")
@click.argument("review_id")
def delete_review_command(review_id):
    review = Review.query.get(review_id)
    if review:
        db.session.delete(review)
        db.session.commit()
        print(f'Review {review_id} deleted.')
    else:
        print("Review not found.")



app.cli.add_command(create_student_command)
app.cli.add_command(list_students_command)
app.cli.add_command(get_student_command)
app.cli.add_command(edit_student_command)
app.cli.add_command(delete_student_command)

app.cli.add_command(create_staff_command)
app.cli.add_command(list_staff_command)

app.cli.add_command(create_review_command)
app.cli.add_command(list_reviews_command)
app.cli.add_command(edit_review_command)
app.cli.add_command(delete_review_command)

