#!/usr/bin/python3
"""Defines a module that defines a State class.
A class that inherits from declarative_base and
maps the object into corresponding table.
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

data = MetaData()
Base = declarative_base(metadata=data)


class State(Base):
    """Defines the state class."""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, unique=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
