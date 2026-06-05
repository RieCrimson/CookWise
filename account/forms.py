from django import forms  
from account.models import Account

# PILLAR 2: INHERITANCE - AccountForm inherits from forms.ModelForm to reuse Django's built-in form logic and link directly to a database model.
class AccountForm(forms.ModelForm): 
    
    # PILLAR 1: ENCAPSULATION - Bundling individual field properties (classes, placeholders, IDs) and behaviors tightly within the form class.
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control border-start-0 ps-0',
            'placeholder': 'Create Password',
            'id': 'id_password'
        })
    )
    password_confirm = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control border-start-0 ps-0',
            'placeholder': 'Confirm Password',
            'id': 'id_password_confirm'
        })
    )

    class Meta:  
        model = Account   
        fields = ['username', 'email', 'password']  

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control border-start-0 ps-0',
                'placeholder': 'Choose a Username',
                'id': 'id_username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control border-start-0 ps-0',
                'placeholder': 'Email address',
                'id': 'id_email',
                'autocomplete': 'email'
            }),
        }

    def clean(self):
        # PILLAR 3: POLYMORPHISM - Overriding the parent class's clean() method to add custom cross-field validation (checking if passwords match).
        # PILLAR 4: ABSTRACTION - super().clean() calls hidden validation processes that clean the fields without us needing to parse the raw HTTP POST data.
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        # PILLAR 3: POLYMORPHISM - Overriding the parent ModelForm save() method to alter its behavior specifically for hashing user passwords.
        # PILLAR 4: ABSTRACTION - user.set_password abstracts away PBKDF2 cryptographic hashing algorithms behind a simple method call.
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  
        if commit:
            user.save()
        return user