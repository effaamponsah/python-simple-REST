import psycopg2
import psycopg2.extras

connection = psycopg2.connect("dbname=students user=postgres")


def queryallStudents():
    try:
        with connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            sql_query = "select * from students;"
            cursor.execute(sql_query)
            result = cursor.fetchall()
    finally:
        return result


def addstudent(student):
    created = False
    try:
        with connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            query1 = "insert into students (student_name, gender) values(%s,%s)"
            cursor.execute(query1, (student["student_name"], student["gender"],))
            created = True
    except cursor.Error as e:
        connection.rollback()
    finally:
        connection.commit()
        return created

def querystudentbyid(studentid):
    try:
        with connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            sql_query = "select * from students where student_id = %s;"
            cursor.execute(sql_query, (studentid))
            result = cursor.fetchall()
    finally:
        return result


def removestudent(studentid):
    removed = False
    try:
        with connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            query1 = "delete from students where student_id = %s"
            cursor.execute(query1, (studentid,))
            removed = True
    except cursor.Error as e:
        connection.rollback()
    finally:
        connection.commit()
        return removed