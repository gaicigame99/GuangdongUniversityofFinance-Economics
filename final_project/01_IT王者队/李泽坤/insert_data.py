from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Students, Courses, Grades

# engine = create_engine('sqlite:///student_manager.db')
engine = create_engine('mysql+pymysql://root:root@localhost/student_manager')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# insert student item into student table
student1 = Students(sno_id='15251102136', name='OliverLee', sex='男', age=23)
session.add(student1)
session.commit()

student2 = Students(sno_id='15251102137', name='Lily', sex='女', age=22)
session.add(student2)
session.commit()

student3 = Students(sno_id='15251102138', name='Adam', sex='男', age=23)
session.add(student3)
session.commit()
# insert course item into course table
# course: id, name, credit, term
course1 = Courses(name='计算机网络', credit=4, term=2)
session.add(course1)
session.commit()

course2 = Courses(name='数据结构', credit=4, term=1)
session.add(course2)
session.commit()

course3 = Courses(name='数据库基础', credit=2, term=1)
session.add(course3)
session.commit()

course4 = Courses(name='离散数学', credit=4, term=3)
session.add(course4)
session.commit()
# insert grade item into grade table
# grade: student_id, course_id, grade
grade = Grades(
    student_id=1,
    course_id=1,
    grade=85
)
session.add(grade)
session.commit()

grade = Grades(
    student_id=2,
    course_id=1,
    grade=90
)
session.add(grade)
session.commit()

grade = Grades(
    student_id=3,
    course_id=2,
    grade=87
)
session.add(grade)
session.commit()

grade = Grades(
    student_id=1,
    course_id=3,
    grade=90
)
session.add(grade)
session.commit()

grade = Grades(
    student_id=2,
    course_id=4,
    grade=56
)
session.add(grade)
session.commit()
print('insert data success.')
