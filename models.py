# flask_sqlalchemy/models.py

from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


engine = create_engine("sqlite:///database.sqlite3", convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
models = Flask("__name__")
db = SQLAlchemy(models)
Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()


class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Employee(db.Model):

    __tablename__ = 'employee'
    EmpID = Column(Integer, primary_key=True)
    EmployeeName = Column(String)
    Department = Column(String)
    JobTitle = Column(String)
    Salary = Column(Integer)

    def __init__(self, EmpID, EmployeeName, Department):
        self.EmpID = EmpID
        self.EmployeeName = EmployeeName
        self.Department = Department

