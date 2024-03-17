#!/usr/bin/python3
"""Defines a module for a city class
that inherits from declarative_base
to map with corresponding table.
"""
from sqlalchemy import Column, Integer, String
from model_state import Base, State



class City(Base):
    """Defines a city class."""

    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, unique=True
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, foreign_key('states.id'), nullable=False)
