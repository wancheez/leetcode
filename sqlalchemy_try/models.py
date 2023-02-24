from sqlalchemy import (
    create_engine,
    MetaData,
    Integer,
    String,
    Column,
    ForeignKey,
    DateTime,
    PrimaryKeyConstraint,
    UniqueConstraint,
    ForeignKeyConstraint, Index,

)
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from sqlalchemy.orm import relationship

Base = declarative_base()


class Employee(Base):
    __tablename__ = "employers"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    manager_id = Column(Integer, nullable=True)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    department_id = Column(Integer, ForeignKey("departments.id"))
    __table_args__ = (
        PrimaryKeyConstraint("id", name="employee_pk"),
        ForeignKeyConstraint(["manager_id"], ["employers.id"]),
        UniqueConstraint("email")
    )


class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    director_id = Column(Integer, ForeignKey('employers.id'))
    director = relationship("Employee", back_populates="departments", foreign_keys="[Employee.id]", uselist=False)
    employees = relationship("Employee")
    __table_args__ = (
        PrimaryKeyConstraint("id", name="department_pk"),
        UniqueConstraint("name"),
        Index("director_index", "director_id"),
    )
