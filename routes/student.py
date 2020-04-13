from flask import jsonify, request
from commons import queries


def get_all_students():
    students =queries.queryallStudents()
    return jsonify(success=True,student=students)


def add_student():
    body = request.get_json()
    response = queries.addstudent(body)

    if response ==True:
        return jsonify(response=response, message="Student added")
    else:
        return jsonify(response=response, message="Error occured")

def get_student_by_id(student_id):
    response = queries.querystudentbyid(student_id)
    return jsonify(response=response)

def delete_student_by_id(student_id):
    response = queries.removestudent(student_id)
    if response ==True:
        return jsonify(success=response, message="Student removed")
    else:

        return jsonify(success=response, message="Error occred")