from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# PILLAR 2: INHERITANCE - CookingTransaction inherits from models.Model, gaining all of Django's core ORM features, database connectivity, and querying power automatically.
class CookingTransaction(models.Model): 

    # PILLAR 1: ENCAPSULATION - The class encapsulates its attributes (date_cooked, recipeid, rating) and internal configurations (class Meta) into a single, cohesive unit.
    date_cooked = models.DateField(default=timezone.now)
    
    # PILLAR 4: ABSTRACTION - models.ForeignKey abstracts away complex relational SQL logic (like creating JOIN tables and enforcing foreign key database constraints) into a simple line of Python.
    recipeid = models.ForeignKey('recipe.Recipe', on_delete=models.CASCADE, related_name='cooking_transactions')
    
    # PILLAR 3: POLYMORPHISM - The validator classes (MinValueValidator, MaxValueValidator) implement a common validation interface polymorphically. Django executes their specific checking routines seamlessly during model clean operations.
    rating = models.IntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )    
    
    class Meta:  
        db_table = "cooking_transactions"