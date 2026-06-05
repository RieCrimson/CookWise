from django.apps import AppConfig

# PILLAR 2: INHERITANCE - RecipeConfig inherits from AppConfig, absorbing all necessary application-loading, signaling, and system registration workflows from Django's core framework.
class RecipeConfig(AppConfig):
    
    # PILLAR 1: ENCAPSULATION - Packing the structural application configurations (like the package 'name') neatly within a single class unit.
    # PILLAR 4: ABSTRACTION - By simply declaring the 'recipe' name string, Django abstracts away all the complicated low-level application mapping routines running behind the scenes.
    name = 'recipe'