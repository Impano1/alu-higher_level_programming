#!/usr/bin/python3
"""
    contains Rectangle class that implements Base class
"""
from models.base import Base


class Rectangle(Base):
    """
        class Rectangle implements Base class
        Methods:
            __init__()
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initializes class instance
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
