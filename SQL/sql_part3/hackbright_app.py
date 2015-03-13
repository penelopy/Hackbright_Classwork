import sqlite3

DB = None
CONN = None

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    return row

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("../hackbright.db")
    DB = CONN.cursor()

def make_new_student(first_name, last_name, github):
    query = """INSERT into Students values (?, ?, ?)"""
    DB.execute(query, (first_name, last_name, github))
    CONN.commit()
    print "Successfully added student: %s %s" %(first_name, last_name)

def projects_by_title(title):
    query = """SELECT title, description FROM Projects WHERE title = ?"""
    DB.execute(query, (title,))
    row = DB.fetchone()
    print"""
Projects: %s 
Description: %s """ % (row[0], row[1])

def add_project(title, description, max_grade):
    query = """INSERT into Projects (title, description, max_grade) values (?, ?, ?)"""
    DB.execute(query, (title, description, max_grade))
    CONN.commit()
    print "Successfully added project: %s %s %d" %(title, description, int(max_grade))

def find_grade(student_github):
    query = """SELECT G.project_title, G.grade FROM GRADES AS G WHERE student_github = ?"""
    DB.execute(query, (student_github,))
    row = DB.fetchone()
    print"""
Project Title: %s 
Grade: %s """ % (row[0],row[1])

def add_grade(student_github, project_title, grade):
    query = """INSERT into GRADES (student_github, project_title, grade) values (?, ?, ?)"""
    DB.execute(query, (student_github, project_title, grade))
    CONN.commit()
    print "Successfully added grade: %s %s %d" %(student_github, project_title, int(grade))

def find_all_grades(student_github):

    query = """SELECT G.project_title, G.grade FROM GRADES AS G WHERE student_github = ?"""
    DB.execute(query, (student_github,))
    rows = DB.fetchall()
    return rows
#     for row in rows:
# """
#         Project Title: %s 
#         Grade: %s """ % (row[0],row[1])



def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database> ")
        tokens = input_string.split()
        command = tokens[0]
        args = tokens[1:]

        if command == "student":
            get_student_by_github(*args) 
        elif command == "new_student":
            make_new_student(*args)
        elif command == "project":
            projects_by_title(*args)
        elif command == "new_project":
            add_project(*args)
        elif command == "find_grade":
            find_grade(*args)
        elif command == "add_grade":
            add_grade(*args)
        elif command == "find_all_grades":
            find_all_grades(*args)

    CONN.close()

if __name__ == "__main__":
    main()
