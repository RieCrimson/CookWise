from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser): 
    # PILLAR 2: INHERITANCE - Inheriting from AbstractUser grants this class all built-in Django user fields and auth methods.

    # PILLAR 1: ENCAPSULATION - Bundling the data fields (email), metadata, and methods into a single, cohesive class unit.
    email = models.EmailField(unique=True) 

    class Meta:  
        db_table = "account"

    def __str__(self):
        # PILLAR 3: POLYMORPHISM - Overriding the native __str__ method to change how this specific object represents itself as a string.
        # PILLAR 4: ABSTRACTION - models.EmailField abstracts away complex database SQL constraints like 'UNIQUE' behind simple Python code.
        return self.username