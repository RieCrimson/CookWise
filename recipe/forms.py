from django import forms  
from .models import Recipe
 
# PILLAR 2: INHERITANCE - RecipeForm inherits from forms.ModelForm, capturing all the core functionality required to dynamically generate form structures from a database model.
class RecipeForm(forms.ModelForm):  
    
    # PILLAR 1: ENCAPSULATION - The Meta class bundles the targeted model, data fields, and structural rendering rules securely inside a single class scope.
    class Meta:  
        model = Recipe  
        
        fields = ['name', 'meal_type', 'date_to_cook', 'steps_to_cook'] 

        # PILLAR 4: ABSTRACTION - The widgets dictionary completely abstracts away manual HTML form controls construction, mapping configurations onto front-end fields seamlessly.
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Recipe Name'
            }),
            
            # PILLAR 3: POLYMORPHISM - forms.TextInput, forms.Select, forms.DateInput, and forms.Textarea all derive from a common Widget class interface. They handle varied argument inputs polymorphically and output distinct HTML elements.
            'meal_type': forms.Select(attrs={
                'class': 'form-select'
            }),
            'date_to_cook': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'steps_to_cook': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter steps to cook the recipe',
                'rows': 4
            }),
        }