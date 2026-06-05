from django.db import models
from django.utils import timezone

# PILLAR 2: INHERITANCE - Recipe inherits from models.Model, automatically absorbing Django's entire ORM backend functionality for database communication.
class Recipe(models.Model): 
    
    # PILLAR 1: ENCAPSULATION - The class bundles all status constants (BREAKFAST, LUNCH, etc.), structural fields (name, meal_type), and database configs (class Meta) into a single module.
    BREAKFAST = 'BREAKFAST'
    LUNCH = 'LUNCH'
    DINNER = 'DINNER'
    DESSERT = 'DESSERT'
    SNACK = 'SNACK'

    MEAL_CHOICES = [
        (BREAKFAST, 'Breakfast'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner'),
        (DESSERT, 'Dessert'),
        (SNACK, 'Snack'),
    ]

    # PILLAR 4: ABSTRACTION - models.CharField and models.TextField abstract away complex SQL database data type definitions (like VARCHAR and TEXT) behind simple Python class instances.
    name = models.CharField(max_length=100)  
    
    # PILLAR 3: POLYMORPHISM - Django models process fields polymorphically during initialization and validation. Even though 'meal_type' and 'name' are different field classes, they implement a common setup interface.
    meal_type = models.CharField(
        max_length=10,
        choices=MEAL_CHOICES,
        default=SNACK
    ) 
    date_to_cook = models.DateField(default=timezone.now)
    steps_to_cook = models.TextField(blank=True)    
    
    class Meta:  
        db_table = "recipe" 