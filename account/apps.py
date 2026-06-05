from django.apps import AppConfig

# PILLAR 2: INHERITANCE - AccountConfig inherits from AppConfig, absorbing all the necessary startup, registry, and application-loading capabilities from Django's core engine.
class AccountConfig(AppConfig):
    
    # PILLAR 1: ENCAPSULATION - Bundling application-specific settings (like the application name metadata) directly inside this dedicated configuration class.
    # PILLAR 4: ABSTRACTION - By defining 'name', Django's internal subsystems automatically map out this app's pathways, database migrations, and template paths behind the scenes.
    name = 'account'