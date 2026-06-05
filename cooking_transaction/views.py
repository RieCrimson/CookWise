from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import CookingTransaction
from .forms import CookingTransactionForm
from ingredients.models import Ingredient
from recipe.models import Recipe

def show_cooking_transactions(request):  
    # PILLAR 4: ABSTRACTION - .all() abstracts away the database query. Instead of writing "SELECT * FROM cooking_transaction", Django handles it under the hood.
    cooking_transactions = CookingTransaction.objects.all()  
    return render(request,"cooking_transaction.html",{'cooking_transactions':cooking_transactions})

def create_cooking_transaction(request):  
    if request.method == "POST":  
        # PILLAR 1: ENCAPSULATION - CookingTransactionForm encapsulates HTTP POST data, field validation, and error messages into one secure object.
        form = CookingTransactionForm(request.POST)  
        
        # PILLAR 3: POLYMORPHISM - is_valid() acts polymorphically. Django handles validation uniquely based on what form object calls it.
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/cooking_transaction')  
            except:  
                pass  
    else:  
        form = CookingTransactionForm()  
    return render(request,'create_cooking_transaction.html',{'form':form})

def create_cooking_transaction(request, id):
    # PILLAR 4: ABSTRACTION - .filter() and .get() abstract away complex SQL WHERE clauses and database lookup logic.
    ingredients = Ingredient.objects.filter(recipeid_id=id)
    recipe = Recipe.objects.get(id=id)  
    
    if request.method == "POST":  
        form = CookingTransactionForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('/cooking_transaction')  
    else:  
        form = CookingTransactionForm(initial={'recipeid': recipe.id})  
        
    return render(request, 'create_cooking_transaction.html', {
        'form': form, 
        'ingredients': ingredients, 
        'recipe': recipe
    })

def edit_cooking_transaction(request, id):  
    # PILLAR 4: ABSTRACTION - get_object_or_404 abstracts away a database lookup combined with try/except blocks that raise HTTP 404 errors.
    cooking_transaction = get_object_or_404(CookingTransaction, id=id)  
    
    # PILLAR 3: POLYMORPHISM - Passing a model 'instance' to CookingTransactionForm changes its behavior polymorphically, switching it from a blank "Create" form to a pre-filled "Edit" form.
    form = CookingTransactionForm(instance=cooking_transaction)  
    return render(request, 'edit_cooking_transaction.html', {
        'cooking_transaction': cooking_transaction, 
        'form': form
    })
  
def update_cooking_transaction(request, id):  
    cooking_transaction = get_object_or_404(CookingTransaction, id=id)  
    form = CookingTransactionForm(request.POST, instance = cooking_transaction)   
    if form.is_valid():  
        form.save()  
        return redirect("/cooking_transaction")  
    return render(request, 'edit_cooking_transaction.html', {'cooking_transaction': cooking_transaction })