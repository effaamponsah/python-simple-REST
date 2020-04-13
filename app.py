from flask import Flask, jsonify, request
from routes import student

app = Flask(__name__)


@app.route('/')
def indexPage():
    return jsonify(success=True, message="Welcome to the basic API setup")

@app.route('/student', methods=["POST", "GET"])
def studentroute():
    if request.method == 'GET':
        return student.get_all_students()
    if request.method == 'POST':
        return student.add_student()
    else:
        return jsonify(success=False, message="Method not supported")

@app.route('/student/<student_id>', methods=["GET","DELETE"])
def studentroutebyid(student_id):
    if request.method == "GET":
        return student.get_student_by_id(student_id)
    if request.method == "DELETE":
        return student.delete_student_by_id(student_id)

if __name__ == "__main__":
    app.run(debug=True,threaded=True)