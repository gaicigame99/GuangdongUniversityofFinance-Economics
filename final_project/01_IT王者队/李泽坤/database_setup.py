from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('mysql+pymysql://root:root@localhost/student_manager')


class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    sno_id = Column(String(11), nullable=False)
    name = Column(String(80), nullable=False)
    sex = Column(String(4), nullable=False)
    age = Column(Integer, nullable=False)


class Courses(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    credit = Column(Integer, nullable=False)
    term = Column(Integer, nullable=False)


class Grades(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    grade = Column(Integer, nullable=False)
    student = relationship(Students)
    course = relationship(Courses)


Base.metadata.create_all(engine)
