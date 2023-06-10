from django.db import models

# Create your models here.


class Ingredient(models.Model):
	idIngredient = models.AutoField(primary_key=True)
	nomIngredient = models.CharField(max_length=50, verbose_name="le nom de cet ingredient")

	def __str__(self):
		return self.nomIngredient


class Pizza(models.Model):
	idPizza = models.AutoField(primary_key=True)
	nomPizza = models.CharField(max_length=50, verbose_name="le nom de cette Pizza")
	prix = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="le prix ", null=True)

	def __str__(self):
		#return 'pizza' + self.nomPizza + '(prix= ' + str(self.prix) + '$'
		return self.nomPizza


class Composition(models.Model):
	class Meta:
		unique_together = ('ingredient', 'pizza')

	idComposition = models.AutoField(primary_key=True)
	pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
	ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
	quantite = models.CharField(max_length=100, verbose_name="la quantité")

	def __str__(self) -> str:
		ing = self.ingredient
		piz = self.pizza
		return f"{self.idComposition} - {self.idPizza.nomPizza} - {self.idIngredient.nomIngredient} ({self.quantite})"