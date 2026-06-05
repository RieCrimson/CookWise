from django.db import models

# PILLAR 2: INHERITANCE - Ingredient inherits from models.Model, automatically receiving all of Django's core ORM properties, query routing behaviors, and database backend capabilities.
class Ingredient(models.Model): 
    
    # PILLAR 1: ENCAPSULATION - The class bundles all state fields (name, quantity, price, unit), structural constants (UNIT_CHOICES), configuration hooks (class Meta), and logic (__str__) inside a single object blueprint.
    name = models.CharField(max_length=100)  
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # PILLAR 4: ABSTRACTION - models.ForeignKey completely abstracts away database-level schema constraints, index assignments, and SQL JOIN table generation rules behind a clean relational definition.
    recipeid = models.ForeignKey('recipe.Recipe', on_delete=models.CASCADE, related_name='ingredients', null=True, blank=True) 
    stock_status = models.CharField(max_length=20) 

    UNIT_CHOICES = [
        ('g', 'Grams (g)'),
        ('kg', 'Kilograms (kg)'),
        ('ml', 'Milliliters (ml)'),
        ('l', 'Liters (l)'),
        ('pcs', 'Pieces (pcs)'),
        ('tbsp', 'Tablespoon (tbsp)'),
        ('tsp', 'Teaspoon (tsp)'),
        ('cup', 'Cup (cup)'),
    ]
    
    unit = models.CharField(
        max_length=10, 
        choices=UNIT_CHOICES, 
        default='pcs'
    )

    def __str__(self):
        # PILLAR 3: POLYMORPHISM - Overriding the standard __str__ method ensures that Python's native string conversion interfaces render this object dynamically as its 'name' instead of its raw memory pointer address.
        return self.name
     
    class Meta:  
        db_table = "ingredients"