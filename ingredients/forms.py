from django import forms  
from .models import Ingredient   

# PILLAR 2: INHERITANCE - IngredientForm inherits from forms.ModelForm to capture all underlying model field constraints automatically.
# PILLAR 4: ABSTRACTION - By subclassing forms.ModelForm, Django abstracts the process of inspecting database column data types and mapping them to HTML inputs.
class IngredientForm(forms.ModelForm): 
    
    # PILLAR 1: ENCAPSULATION - The Meta class bundles model connectivity, field ordering, and UI widget behaviors into a single, enclosed structure.
    class Meta:  
        model = Ingredient  
        fields = ['name', 'quantity', 'unit', 'price', 'stock_status']

        # PILLAR 4: ABSTRACTION - The widgets dictionary abstracts away manual HTML input assembly (<input>, <select>) behind clean Python configurations.
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Ingredient Name'
            }),
            
            # PILLAR 3: POLYMORPHISM - forms.NumberInput, forms.TextInput, and forms.Select are polymorphic instances of the base Widget class. They all implement the same interface but render completely different HTML output structures.
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'min': 0
            }),
            'unit': forms.Select(attrs={
                'class': 'form-select'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'min': 0,
                'step': '0.01'
            }),
            'stock_status': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }

# PILLAR 4: ABSTRACTION - modelformset_factory completely abstracts complex multi-form management, generation logic, and form prefix handling into a single factory function call.
IngredientFormSet = forms.modelformset_factory(
    Ingredient,
    form=IngredientForm,  
    extra=3               
)