from django.db import models
from datetime import *
# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=255, verbose_name="Название категории")
	alias = models.SlugField(verbose_name="Алиас категории")
	class Meta:
		verbose_name = "Категория"
		verbose_name_plural = "Категории"
	def __str__(self):
		return "Категория %s" % self.name
		
class Item(models.Model):
	name = models.CharField(max_length=255, verbose_name="Название товара")
	price = models.IntegerField(default=0, verbose_name="Цена")
	image = models.CharField(max_length=255, verbose_name="Ссылка на картинку")
	alias = models.SlugField(verbose_name="Алиас товара")
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	class Meta:
		verbose_name = "Товар"
		verbose_name_plural = "Товары"
	def __str__(self):
		return "Товар %s" % self.name



