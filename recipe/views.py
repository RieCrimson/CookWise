from django.shortcuts import render
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory  
from .models import Recipe
from .forms import RecipeForm
from ingredients.models import Ingredient
from ingredients.forms import IngredientForm

# PILLAR 4: ABSTRACTION - inlineformset_factory completely abstracts away the manual handling of complex SQL foreign key relational integrity constraints when building multiple forms.
IngredientFormSet = inlineformset_factory(
    Recipe, 
    Ingredient, 
    fields=('name', 'quantity', 'price', 'stock_status'), 
    extra=3,                     
    can_delete=False
)

def show_recipe(request):  
    # PILLAR 4: ABSTRACTION - Recipe.objects.all() abstracts database queries, translating clean Python code directly into native SQL under the hood.
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
    }  
    return render(request,"recipe.html",context)

def create_recipe(request):
    # PILLAR 4: ABSTRACTION - We pass the Recipe and Ingredient models along with the custom Form class. The factory abstracts away the complex logic required to handle a parent-child relationship, form validation states, and dynamic row tracking counters.
    RecipeIngredientFormSet = inlineformset_factory(
        Recipe, 
        Ingredient, 
        form=IngredientForm,
        fk_name='recipeid',  
        extra=3,             
        can_delete=False     
    )

    if request.method == "POST":
        # PILLAR 1: ENCAPSULATION - RecipeForm and RecipeIngredientFormSet encapsulate HTTP data payloads, individual processing tokens, and error metrics safely within distinct state objects.
        form = RecipeForm(request.POST)
        formset = RecipeIngredientFormSet(request.POST)
        
        # PILLAR 3: POLYMORPHISM - form.is_valid() and formset.is_valid() act polymorphically. They execute entirely unique validation routines based on the architectural makeup of the calling instance.
        # PILLAR 4: ABSTRACTION - form.is_valid() and formset.is_valid() abstract away complex data cleaning, regex parsing, type checking (ensuring price is a decimal), and security checks.
        if form.is_valid() and formset.is_valid():
            
            # PILLAR 4: ABSTRACTION - form.save() and formset.save() abstract away the creation of database connections, writing raw SQL "INSERT INTO" queries, handling rollbacks, and transaction commits.
            recipe = form.save()
            
            formset.instance = recipe
            formset.save()
                
            return redirect('show_recipe') 
        else:
            print("Form errors:", form.errors)
            print("Formset errors:", formset.errors)
    else:
        form = RecipeForm()
        formset = RecipeIngredientFormSet()
        
    return render(request, 'create_recipe.html', {
        'form': form,
        'formset': formset
    })

def edit_recipe(request, id):  
    recipe = Recipe.objects.get(id=id)
    ingredients = Ingredient.objects.filter(recipeid_id=id)  
    
    # PILLAR 3: POLYMORPHISM - Passing a data 'instance' changes the execution track polymorphically, switching the default structure from record creation to record modification.
    form = RecipeForm(instance=recipe)  
    return render(request,'edit_recipe.html', {'recipe':recipe, 'form': form, 'ingredients': ingredients})

def update_recipe(request, id):  
    recipe = Recipe.objects.get(id=id)  
    form = RecipeForm(request.POST, instance = recipe)  
    if form.is_valid():  
        form.save()  
        return redirect("/recipe")  
    return render(request, 'edit_recipe.html', {'recipe': recipe, 'form': form})