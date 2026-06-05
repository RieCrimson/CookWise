from django.urls import path
from . import views

# PILLAR 1: ENCAPSULATION
# 'urlpatterns' is a list that encapsulates a collection of URL pattern objects.
# Each 'path()' function call creates a route object that bundles the URL route string, the view function, and the route name into a single entity.
urlpatterns = [
    # PILLAR 3: POLYMORPHISM & PILLAR 4: ABSTRACTION
    # The 'path()' function handles argument parsing polymorphically (it accepts different types of views/arguments) and abstracts away the complex regex matching used under the hood.
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login, name='login'),
]