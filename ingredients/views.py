from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Ingredient
from .forms import IngredientForm


def show_ingredients(request):  
    # PILLAR 4: ABSTRACTION - Ingredient.objects.all() abstracts away the complex database query execution ("SELECT * FROM ingredients") behind a simple Python method call.
    ingredients = Ingredient.objects.all()  
    return render(request,"ingredients.html",{'ingredients':ingredients})

def create_ingredient(request, id=None):  
    if request.method == "POST":  
        # PILLAR 1: ENCAPSULATION - IngredientForm encapsulates HTTP POST request data, internal field validation rules, and error tracking within a single form object.
        form = IngredientForm(request.POST)  
        
        # PILLAR 3: POLYMORPHISM - The form.is_valid() method behaves polymorphically, executing validation routines unique to the structure and fields of IngredientForm.
        if form.is_valid():  
            try: 
                ingredient = form.save(commit=False)
                if id:
                    ingredient.recipeid_id = id  
                ingredient.save()  
                
                if id:
                    return redirect(f'/edit_recipe/{id}/')
                else:
                    return redirect('/create_recipe/') 
            except Exception as e:  
                print("DATABASE ERROR:", e)
        else:
            print("FORM ERRORS:", form.errors)
            
    else:  
        form = IngredientForm()

    return render(request, 'create_ingredients.html', {'form': form, 'recipeid': id})

def edit_ingredient(request, id):  
    # PILLAR 4: ABSTRACTION - Ingredient.objects.get() abstracts away database record lookup operations, matching structural indexes seamlessly.
    ingredient = Ingredient.objects.get(id=id)  
    return render(request,'edit_ingredients.html', {'ingredient':ingredient})
  
def update_ingredient(request, id):  
    ingredient = Ingredient.objects.get(id=id)
    recipe_id = ingredient.recipeid_id  
    
    # PILLAR 3: POLYMORPHISM - Passing an 'instance' changes the constructor behavior polymorphically. Instead of constructing a blank creation form, IngredientForm shifts contexts to update an existing record.
    form = IngredientForm(request.POST, instance = ingredient)  
    if form.is_valid():  
        form.save()  
        return redirect(f"/edit_recipe/{recipe_id}/")  
    return render(request, 'edit_ingredients.html', {'ingredient': ingredient})