from django import forms  
from .models import CookingTransaction    

# PILLAR 2: INHERITANCE - CookingTransactionForm inherits from forms.ModelForm, absorbing all the machinery required to map form inputs to a specific database model.
class CookingTransactionForm(forms.ModelForm): 
    
    # PILLAR 1: ENCAPSULATION - The class encapsulates the model connection, field mapping, and structural UI widget behaviors tightly into a single object.
    class Meta:  
        model = CookingTransaction  
        fields = "date_cooked", "recipeid", "rating"

        # PILLAR 4: ABSTRACTION - Widgets abstract away the manual creation of raw HTML elements (<input type="hidden">, <input type="date">) behind simple Python declarations.
        widgets = {
            # This ensures Django renders it as a proper hidden input element
            'recipeid': forms.HiddenInput(),
            
            # PILLAR 3: POLYMORPHISM - forms.HiddenInput() and forms.DateInput() are polymorphic instances of the base Widget class. They implement the same underlying rendering interface, but dynamically generate completely different HTML based on the widget type.
            'rating': forms.HiddenInput(attrs={'id': 'id_rating', 'value': '5'}),
            'date_cooked': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }