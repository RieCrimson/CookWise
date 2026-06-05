from django.apps import AppConfig

# PILLAR 2: INHERITANCE - IngredientsConfig inherits from AppConfig, absorbing all necessary lifecycle hooks and registration routines from Django's core application registry.
class IngredientsConfig(AppConfig):
    
    # PILLAR 1: ENCAPSULATION - Bundling application metadata and configuration settings (like the 'name' attribute) neatly inside a single, dedicated class.
    # PILLAR 4: ABSTRACTION - Defining the 'name' string allows Django to abstractly wire up app-specific features like namespace mapping, migrations, and template paths without explicit manual coding.
    name = 'ingredients'