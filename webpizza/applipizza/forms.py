from django import forms
from django.forms import ModelForm
from .models import Ingredient, Pizza, Composition




class IngredientForm(forms.ModelForm):
    
    class Meta:
        model = Ingredient
        fields = ["nomIngredient"]



class PizzaForm(forms.ModelForm):
    
    class Meta:
        model = Pizza
        exclude = ["idPizza"]

class CompositionForm(forms.ModelForm):
    
    class Meta:
        model = Composition
        fields = ["ingredient", "quantite"]




