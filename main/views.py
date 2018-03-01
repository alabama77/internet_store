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
	tovars = Item.objects.all()

	context = {
		'title' : "HelloWorld",
		'tovars' : tovars,
	}
	return HttpResponse(render_to_string('index.html', context))

def item(request, alias):
	try:
		tovar = Item.objects.get(alias=alias)
	except:
		return Http404

	context = {"tovar" : tovar}
	return HttpResponse(render_to_string('item.html', context))

	

