from django.shortcuts import render
from main.models import *
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string
from datetime import *
import random
import string

# Create your views here.


def home(request):
	category = Category.objects.all()
	context = {
	}
	return HttpResponse(render_to_string('home.html', context))

def item(request, alias):
	try:
		tovar = Item.objects.get(alias=alias)
	except:
		return Http404

	context = {"tovar" : tovar}
	return HttpResponse(render_to_string('item.html', context))

def get_category(request, alias):
	try:
		category = Category.objects.get(alias=alias)
		tovars = Item.objects.filter(category=category)
	except:
		return Http404
	context = {"tovars" : tovars,
				"category" : category,}
	return HttpResponse(render_to_string("index.html", context))


	

