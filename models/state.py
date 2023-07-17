#!/usr/bin/python3
"""
Class that defines a state
"""

from models.base_model import BaseModel


class State(BaseModel):
    """Representation of state """

    name = ""

    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__(*args, **kwargs)
