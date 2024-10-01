import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from datetime import datetime
from App.database import db, get_migrate
from App.models import User, Student, Staff, Review
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize)
from App.controllers.student import create_student, list_students, get_student, edit_student, delete_student
from App.controllers.staff import create_staff, list_staff
from App.controllers.review import create_review, list_reviews, edit_review, delete_review


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




# Student CLI group
student_cli = AppGroup('student', help="Student object commands")

@student_cli.command("create", help="Creates a student")
@click.argument("first_name")
@click.argument("last_name")
@click.argument("degree")
def create_student_command(first_name, last_name, degree):
    create_student(first_name, last_name, degree)

@student_cli.command("list", help="Lists all students")
def list_students_command():
    list_students()

@student_cli.command("get", help="Get a student by ID")
@click.argument("student_id")
def get_student_command(student_id):
    get_student(student_id)

@student_cli.command("edit", help="Edits a student's details")
@click.argument("student_id")
@click.argument("first_name")
@click.argument("last_name")
@click.argument("degree")
def edit_student_command(student_id, first_name, last_name, degree):
    edit_student(student_id, first_name, last_name, degree)

@student_cli.command("delete", help="Deletes a student by ID")
@click.argument("student_id")
def delete_student_command(student_id):
    delete_student(student_id)

app.cli.add_command(student_cli)

# Staff CLI group
staff_cli = AppGroup('staff', help="Staff object commands")

@staff_cli.command("create", help="Creates a new staff member")
@click.argument("first_name")
@click.argument("last_name")
@click.argument("role")
def create_staff_command(first_name, last_name, role):
    create_staff(first_name, last_name, role)

@staff_cli.command("list", help="Lists all staff members")
def list_staff_command():
    list_staff()

app.cli.add_command(staff_cli)

# Review CLI group
review_cli = AppGroup('review', help="Review object commands")

@review_cli.command("create", help="Creates a new review")
@click.argument("student_id")
@click.argument("staff_id")
@click.argument("review_type")
@click.argument("description")
@click.option("--review-date", type=click.DateTime(), help="Review date (optional)")
def create_review_command(student_id, staff_id, review_type, description, review_date):
    create_review(student_id, staff_id, review_type, description, review_date)


@review_cli.command("list", help="Lists all reviews for a student")
@click.argument("student_id")
def list_reviews_command(student_id):
    list_reviews(student_id)

@review_cli.command("edit", help="Edits a review")
@click.argument("review_id")
@click.argument("review_type")
@click.argument("description")
@click.option("--review-date", type=click.DateTime(), help="Review date (optional)")
def edit_review_command(review_id, review_type, description, review_date):
    edit_review(review_id, review_type, description, review_date)

@review_cli.command("delete", help="Deletes a review by ID")
@click.argument("review_id")
def delete_review_command(review_id):
    delete_review(review_id)

app.cli.add_command(review_cli)
