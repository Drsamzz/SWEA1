from App.models import Student, Staff, Review
from App.database import db
from datetime import datetime

def create_review(student_id, staff_id, review_type, description, review_date=None):
    student = Student.query.get(student_id)
    staff = Staff.query.get(staff_id)
    if student and staff:
        review_date = datetime.utcnow()  # default to current date and time
        review = Review(
            studentID=student_id, 
            staffID=staff_id, 
            reviewType=review_type, 
            description=description,
            reviewDate=review_date
        )
        db.session.add(review)
        db.session.commit()
        print(f'Review for student {student_id} by staff {staff_id} created.')
    else:
        print("Student or staff not found.")

def list_reviews(student_id):
    student = Student.query.get(student_id)
    if student:
        reviews = student.reviews
        if reviews:
            for review in reviews:
                staff_first_name = review.staff.firstName if review.staff else "Unknown Staff"
                print(f'Review {review.reviewID}: {review.reviewType}, {review.description}, {review.reviewDate} by {staff_first_name}')
        else:
            print("There are no reviews for this student.")
    else:
        print("Student not found.")

def edit_review(review_id, review_type, description, review_date=None):
    review = Review.query.get(review_id)
    if review:
        review_date = datetime.utcnow()  # default to current date and time
        review.reviewType = review_type
        review.description = description
        reviewDate=review_date
        db.session.commit()
        print(f'Review {review_id} updated.')
    else:
        print("Review not found.")

def delete_review(review_id):
    review = Review.query.get(review_id)
    if review:
        db.session.delete(review)
        db.session.commit()
        print(f'Review {review_id} deleted.')
    else:
        print("Review not found.")