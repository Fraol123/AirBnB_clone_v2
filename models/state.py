#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='states', cascade="all, delete" )
