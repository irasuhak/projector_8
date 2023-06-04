## Practice

# 1. Add models for student, subject and student_subject from previous lessons in SQLAlchemy.
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)

    subjects = relationship("StudentSubject", back_populates="student")


class Subject(Base):
    __tablename__ = 'subject'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    students = relationship("StudentSubject", back_populates="subject")


class StudentSubject(Base):
    __tablename__ = 'student_subject'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'), nullable=False)
    subject_id = Column(Integer, ForeignKey('subject.id'), nullable=False)

    student = relationship("Student", back_populates="subjects")
    subject = relationship("Subject", back_populates="students")


    
# 2. Find all students` name that visited 'English' classes 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create an engine and session
engine = create_engine('postgresql://{postgres}:{password}@{localhost}:{5432}/{postgres}')
Session = sessionmaker(bind=engine)
session = Session()

# Query for students who visited 'English' classes
students = session.query(Student).\
    join(StudentSubject, Student.id == StudentSubject.student_id).\
    join(Subject, StudentSubject.subject_id == Subject.id).\
    filter(Subject.name == 'English').all()

# Get the names of the students
student_names = [student.name for student in students]

# Print the names of the students
for name in student_names:
    print(name)
    
