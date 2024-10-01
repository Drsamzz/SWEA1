# Student Conduct Tracker Commands Overview #

# Note #

Review Type: The review type must be either "Positive" or "Negative".

Description: The description should be enclosed in quotes.

Review Date: The review date is automatically set and does not need to be provided.


# Staff Commands #


* Create a Staff Member:

```bash
$ flask staff create <first_name> <last_name> <role>
```
Creates a new staff memeber with the specified details.


* List Staff Members:

```bash
$ flask staff list
```
Lists all staff members in the database.


# Student Commands #


* Create a Student: 


```bash
$ flask student create <first_name> <last_name> <degree>
```
Creates a new student with the specified details.

* List Students: 


```bash
$ flask student list
```
Lists all students in the database.


* Get a Student: 
Retrieves a specific student by their ID.

```bash
$ flask student get <student_id>
```
Retrieves a specific student by their ID.


* Edit a Student: 

```bash
$ flask student edit <student_id> <first_name> <last_name> <degree>
```
Edits an existing student's details.

* Delete a Student:


```bash
$ flask student delete <student_id>
```
Deletes a student from the database by their ID.


# Review Commands #

* Create a Review:

```bash
$ flask review create <student_id> <staff_id> <review_type> <description>
```
Creates a new review for a specific student by a staff member.

EG
```bash
$ flask review create 1 2 positive "Great performance on the last project!"
```

* List Reviews for a Student:

```bash
$ flask review list <student_id>
```
Lists all reviews for a specific student by their ID.


* Edit a Review:

```bash
$ flask review edit <review_id> <review_type> <description>
```
Edits an existing review based on its ID.


* Delete a Review:

```bash
$ flask review delete <review_id>
```
Edits an existing review based on its ID.

EG
```bash
$ flask review edit 5 negative "Needs improvement in teamwork skills."
```

























