#!/usr/bin/python3
"""
Class User that inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Blueprint for a User object
    Public Attributes that will use FileStorage in engine
    folder to manage serialization and deserialization of User
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new User instance
        """
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
