"""applipiza URL Configuration"""

from django.urls import path
from applipizza import views

urlpatterns = [

    path("", views.pizzas, name='pizzas'),

    path("pizzas/", views.pizzas),
    path("pizzas/<int:pizza_id>/", views.pizza),
    path("pizzas/add/", views.formulaire_creation_pizza),   
    path("pizzas/create/", views.creerPizza),   
    path("pizzas/<int:pizza_id>/addIngredient/", views.ajouterIngredientDansPizza), 
    path('pizzas/<int:pizza_id>/delete/', views.supprimerPizza),  
    path('pizzas/<int:pizza_id>/update/', views.afficherFormulaireModificationPizza),
    path('pizzas/<int:pizza_id>/updated/', views.modifierPizza),
    path('pizzas/<int:pizza_id>/deleteIngredient/<int:composition_id>/', views.supprimerIngredientDansPizza),


    path("ingredients/", views.ingredients),
    path("ingredients/add/", views.formulaire_creation_ingredient),   
    path("ingredients/create/", views.creerIngredient),   
    path('ingredients/<int:ingredient_id>/delete/', views.supprimerIngredient),
    path('ingredients/<int:ingredient_id>/update/', views.afficherFormulaireModificationIngredient),
    path('ingredients/<int:ingredient_id>/updated/', views.modifierIngredient),

]
