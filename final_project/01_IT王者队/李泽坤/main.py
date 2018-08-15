from flask import Flask, render_template, request, url_for, redirect
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from database_setup import Base, Students, Courses, Grades

app = Flask(__name__)
# engine = create_engine('sqlite:///student_manager.db')
engine = create_engine('mysql+pymysql://root:root@localhost/student_manager')
Base.metadata.bind=engine
DBSession = scoped_session(sessionmaker(bind=engine))
session = DBSession()

@app.route("/")
def Hello():
    return render_template('index.html')

@app.route('/students', methods=['GET', 'POST'])
def students():
    students = session.query(Students).all()
    items = []
    for student in students:
        item = student.sno_id, student.name, student.sex, student.age
        items.append(list(item))
    return render_template('students.html', items = items)

# the page that create new student
@app.route('/students/new', methods=['GET', 'POST'])
def create():
    if request.method == "POST":
        print(request.form)
        student = Students(
            sno_id=request.form['newId'],
            name=request.form['newName'],
            sex=request.form['newSex'],
            age= 0 if request.form['newAge'] == '' else int(request.form['newAge'])
        )
        session.add(student)
        session.commit()
        return redirect(url_for('students'))
    else:
        return render_template('create_student.html')

# the page that edit the info
@app.route('/students/<string:sno_id>/edit', methods=['GET', "POST"])
def edit(sno_id):
    student = session.query(Students).filter_by(sno_id=sno_id).one()
    if request.method == "POST":
        student.name = request.form['newname']
        student.sex = request.form['newsex']
        student.age = 0 if request.form['newage'] == '' else int(request.form['newage'])
        session.add(student)
        session.commit()
        return redirect(url_for('students'))
    else:
        return render_template('editor.html', sno_id=sno_id)

# the page that delete student info
@app.route('/students/<string:sno_id>/delete', methods=['GET', 'POST'])
def delete(sno_id):
    student = session.query(Students).filter_by(sno_id=sno_id).one()
    item = student.sno_id, student.name, student.sex, student.age
    item = list(item)
    grades = session.query(Grades).filter_by(student_id=student.id).all()
    print(grades)
    if request.method == 'POST':
        if grades != []:
            # delete all grade which student has
            for grade in grades:
                session.delete(grade)
                session.commit()
        # delete student
        session.delete(student)
        session.commit()
        return redirect(url_for('students'))
    else:
        return render_template('delete.html', item=item, sno_id=sno_id)

# the page that select that student's grades
@app.route('/students/<string:sno_id>/grades')
def grade(sno_id):
    student = session.query(Students).filter_by(sno_id=sno_id).one()
    grades = session.query(Grades).filter_by(student_id=student.id).all()
    items = []
    for grade in grades:
        item = grade.student.sno_id, grade.student.name, grade.course.name, grade.grade
        items.append(list(item))
    return render_template('grade.html', sno_id=sno_id,items=items)

@app.route('/students/<string:sno_id>/grades/new', methods=['GET', 'POST'])
def create_grade(sno_id):
    student = session.query(Students).filter_by(sno_id=sno_id).one()
    if request.method == 'POST':
        grade = Grades(
            student_id=student.id,
            course_id=request.form['course'],
            grade=request.form['grade']
        )
        session.add(grade)
        session.commit()
        return redirect(url_for('grade', sno_id=sno_id))
    else:
        return render_template('create_grade.html', sno_id=sno_id)


if __name__ == '__main__':
    app.run()