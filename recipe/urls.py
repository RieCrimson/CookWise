from django.urls import path
from . import views

# PILLAR 1: ENCAPSULATION - The 'urlpatterns' list encapsulates a collection of individual route objects, bundling all individual recipe routing rules neatly within one isolated module.
urlpatterns = [
    # PILLAR 4: ABSTRACTION - The dynamic variable '<int:id>' abstracts away complex string manipulation, data parsing, and regex pattern matching required to safely extract path variables.
    path('edit_recipe/<int:id>/', views.edit_recipe, name='edit_recipe'),
    path('update_recipe/<int:id>/', views.update_recipe, name='update_recipe'),
    path('recipe/', views.show_recipe, name='show_recipe'),
    
    # PILLAR 3: POLYMORPHISM - The 'path()' function behaves polymorphically by accepting varied parameter signatures (both flat paths and dynamic variable paths) and processing them seamlessly using a common execution pattern.
    path('create_recipe/', views.create_recipe, name='create_recipe'),
]