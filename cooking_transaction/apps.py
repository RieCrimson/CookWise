from django.apps import AppConfig

# PILLAR 2: INHERITANCE - CookingTransactionConfig inherits from AppConfig, absorbing all backend capabilities to register this application into Django's ecosystem.
class CookingTransactionConfig(AppConfig):
    
    # PILLAR 1: ENCAPSULATION - Enclosing app-specific settings and metadata (like the app package name) neatly within a dedicated configuration class.
    # PILLAR 4: ABSTRACTION - Defining 'name' allows Django's engine to abstractly handle database migrations, template routing, and application states behind the scenes.
    name = 'cooking_transaction'