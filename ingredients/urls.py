from django.urls import path
from . import views

# PILLAR 1: ENCAPSULATION - The 'urlpatterns' list encapsulates a collection of individual route objects, bundling all individual ingredient URL patterns into one cohesive routing container.
urlpatterns = [
    # PILLAR 4: ABSTRACTION - The dynamic variable '<int:id>' abstracts away the complex underlying regex matching, string-slicing, and data-type casting needed to parse values out of a web path.
    path('edit_ingredients/<int:id>/', views.edit_ingredient, name='edit_ingredients'),
    path('update_ingredient/<int:id>/', views.update_ingredient, name='update_ingredient'),
    path('ingredients/', views.show_ingredients, name='show_ingredients'),
    
    # PILLAR 3: POLYMORPHISM - The 'path()' function operates polymorphically here. The routing engine handles the request interface dynamically depending on whether an integer argument is passed alongside the string route.
    path('create_ingredient/', views.create_ingredient, name='create_ingredient_global'),
    path('create_ingredient/<int:id>/', views.create_ingredient, name='create_ingredient_for_recipe')
]