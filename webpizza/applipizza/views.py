from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from applipizza.models import Pizza, Ingredient, Composition
from .forms import IngredientForm, PizzaForm, CompositionForm

# Create your views here.


def pizzas(request):
	lespizzas = Pizza.objects.all()
	context = {'lespizzas': lespizzas}	
	return render(request, "applipizza/pizzas.html", context)

@login_required(login_url='login')
def pizza(request, pizza_id):
	lapizza = Pizza.objects.get(idPizza = pizza_id)

	formulaire = CompositionForm()
	compo = Composition.objects.filter(pizza = pizza_id)

	listeIngredients= []

	for c in compo:
		ing= Ingredient.objects.get(idIngredient= c.ingredient.idIngredient)  
		listeIngredients.append({'nom': ing.nomIngredient, 'qte': c.quantite, 'idComposition':c.idComposition})


	context= {
		'pizza': lapizza, 
		'compo': compo,
		'liste': listeIngredients, 
		'form': formulaire
		}
	return render(request, 'applipizza/pizza.html', context)



def ingredients(request):
	lesingredients = Ingredient.objects.all()
	context = {
		'lesingredients': lesingredients,
	}
	return render(request, "applipizza/ingredients.html", context)

@login_required(login_url='login')
def formulaire_creation_ingredient(request):

	formulaire = IngredientForm()

	context ={"form": formulaire }
	return render(request, "applipizza/formulaireCreationIngredient.html", context)

@login_required(login_url='login')
def creerIngredient(request):

	form = IngredientForm(request.POST)
	if form.is_valid():
		nomIng = form.cleaned_data['nomIngredient']
		ing = Ingredient()
		ing.nomIngredient = nomIng
		ing.save()

		context = {'nom': nomIng}
		return render(request, 'applipizza/traitementFormulaireCreationIngredient.html', context)
	

@login_required(login_url='login')
def formulaire_creation_pizza(request):

	formulaire = PizzaForm()

	context ={"form": formulaire }
	return render(request, "applipizza/formulaireCreationPizza.html", context)


@login_required(login_url='login')
def creerPizza(request):

	form = PizzaForm(request.POST)
	if form.is_valid():
		nomPiz = form.cleaned_data['nomPizza']
		prixPiz = form.cleaned_data['prix']
		pizza = Pizza()
		pizza.nomPizza = nomPiz
		pizza.prix = prixPiz
		pizza.save()

		context = {'nom': nomPiz}
		return render(request, 'applipizza/traitementFormulaireCreationPizza.html', context)
	
@login_required(login_url='login')
def ajouterIngredientDansPizza(request, pizza_id):

	formulaire = CompositionForm(request.POST)
	if formulaire.is_valid():
		ingredient = formulaire.cleaned_data['ingredient']
		qte = formulaire.cleaned_data['quantite']

		compositions = Composition.objects.filter(pizza=pizza_id, ingredient=ingredient)

		if compositions.exists():
			composition = compositions.first()
			composition.delete()

		pizza = Pizza.objects.get(idPizza = pizza_id)

		compo = Composition()
		compo.ingredient = ingredient
		compo.quantite = qte
		compo.pizza = pizza

		compo.save()

	formulaire = CompositionForm()
	lapizza = Pizza.objects.get(idPizza = pizza_id)
	compo = Composition.objects.filter(pizza=pizza_id)

	listeIngredients = []
	for c in compo:
		ing= Ingredient.objects.get(idIngredient= c.ingredient.idIngredient)  
		listeIngredients.append({
			'nom': ing.nomIngredient, 
			'qte': c.quantite, 
			'idComposition': c.idComposition, 
		})

	context= {
		'pizza': lapizza, 
		'compo': compo,
		'liste': listeIngredients, 
		'form': formulaire
		}
	return render(request, 'applipizza/pizza.html', context)

@login_required(login_url='login')
def supprimerPizza(request, pizza_id):
	laPizza = Pizza.objects.get(idPizza = pizza_id)
	laPizza.delete()
	lesPizzas = Pizza.objects.all()
	context = {"lespizzas" : lesPizzas}

	return render(request,'applipizza/pizzas.html', context )

@login_required(login_url='login')
def supprimerIngredient(request, ingredient_id):

	ing = Ingredient.objects.get(idIngredient = ingredient_id)
	ing.delete()
	lesIngredients = Ingredient.objects.all()
	context = {"lesingredients": lesIngredients}

	return render(request, 'applipizza/ingredients.html', context) 
	
@login_required(login_url='login')
def afficherFormulaireModificationPizza(request, pizza_id):
	lapizza = Pizza.objects.get(idPizza = pizza_id)
	formulaire = PizzaForm(instance=lapizza)
	context = {"form" : formulaire, "pizza" : lapizza}
	return render(request, 'applipizza/formulaireModificationPizza.html', context)

@login_required(login_url='login')
def modifierPizza(request, pizza_id):
	laPizza = Pizza.objects.get(idPizza = pizza_id)
	form = PizzaForm(request.POST)
	if form.is_valid():
		nomPiz = form. cleaned_data['nomPizza']
		prixPiz = form.cleaned_data['prix']
		laPizza.nomPizza = nomPiz
		laPizza.prix = prixPiz
		laPizza.save ()
		context = {"nom" : nomPiz, "prix": prixPiz}
	return render(request, "applipizza/traitementFormulaireModificationPizza.html", context)

@login_required(login_url='login')
def afficherFormulaireModificationIngredient(request, ingredient_id):
	ing = Ingredient.objects.get(idIngredient = ingredient_id)
	formulaire = IngredientForm(instance=ing)
	context = {"form" : formulaire, "ing" : ing}
	return render(request, 'applipizza/formulaireModificationIngredient.html', context)

@login_required(login_url='login')
def modifierIngredient(request, ingredient_id):
	ing = Ingredient.objects.get(idIngredient = ingredient_id)
	form = IngredientForm(request.POST)
	if form.is_valid():
		noming = form.cleaned_data['nomIngredient']
		ing.nomIngredient = noming
		ing.save()
		context = {"nom" : noming}
	return render(request, "applipizza/traitementFormulaireModificationIngredient.html", context)

@login_required(login_url='login')
def supprimerIngredientDansPizza(request, pizza_id, composition_id):
    lapizza = Pizza.objects.get(idPizza=pizza_id)
    
    composition = Composition.objects.get(idComposition=composition_id, pizza=lapizza)
    composition.delete()
    
    formulaire = CompositionForm()
    compo = Composition.objects.filter(pizza=pizza_id)
    listeIngredients= []
    
    for c in compo:
	    ing= Ingredient.objects.get(idIngredient= c.ingredient.idIngredient)  
	    listeIngredients.append({'nom': ing.nomIngredient, 'qte': c.quantite, 'idComposition':c.idComposition})


    context= {
		'pizza': lapizza, 
		'compo': compo,
		'liste': listeIngredients, 
		'form': formulaire
	}  
    return render(request, 'applipizza/pizza.html', context)