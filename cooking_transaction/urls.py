from django.urls import path
from . import views

# PILLAR 1: ENCAPSULATION - The 'urlpatterns' list encapsulates a collection of individual route objects, bundling all URL endpoints into a single routing module.
urlpatterns = [
    # PILLAR 4: ABSTRACTION - Dynamic path converters like '<int:id>' abstract away the complex regular expressions and string parsing required to extract variables from an incoming URL.
    path('edit_cooking_transaction/<int:id>/', views.edit_cooking_transaction, name='edit_cooking_transaction'),
    path('update_cooking_transaction/<int:id>/', views.update_cooking_transaction, name='update_cooking_transaction'),
    path('cooking_transaction/', views.show_cooking_transactions, name='show_cooking_transactions'),
    
    # PILLAR 3: POLYMORPHISM - The 'path()' function functions polymorphically here. The router seamlessly redirects traffic to either the standard view or the parameterized view depending on whether an integer ID is provided in the URL request.
    path('create_cooking_transaction/', views.create_cooking_transaction, name='create_cooking_transaction'),
    path('create_cooking_transaction/<int:id>/', views.create_cooking_transaction, name='create_cooking_transaction')
]