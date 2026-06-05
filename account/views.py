from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from .forms import AccountForm

def sign_up(request):  
    if request.method == "POST":  
        # PILLAR 1: ENCAPSULATION & PILLAR 2: INHERITANCE
        # 'AccountForm' encapsulates the data fields and validation logic into a single object.
        # It inherits this behavior from Django's base form classes (e.g., forms.ModelForm).
        form = AccountForm(request.POST)  
        
        # PILLAR 3: POLYMORPHISM
        # 'is_valid()' acts polymorphically. Django forms implement this method differently depending on the specific fields and validation rules defined inside 'AccountForm'.
        if form.is_valid():  
            form.save()  
            messages.success(request, "Account created successfully! Please sign in.")
            return redirect('/login')
    else:  
        form = AccountForm()  
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == "POST":  
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # PILLAR 4: ABSTRACTION
        # 'authenticate()' hides the complex database lookups, hashing algorithms, and security checks. You just pass credentials and get a user object back.
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # PILLAR 4: ABSTRACTION
            # 'auth_login()' abstracts away session creation, cookie management, and state preservation.
            auth_login(request, user)
            return redirect('/recipe')  
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('/login')
    else:  
        form = AccountForm()  
    return render(request, 'login.html', {'form': form})