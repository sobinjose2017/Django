from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.template import Template
from django.shortcuts import render
from .import views
from myapp.models import *
from django.http import JsonResponse

def index(request):
	template = loader.get_template('hello.html')
	context={'title':"Welcome to django Programming"}
	return HttpResponse(template.render(context, request))

def insert(request):
	newtask=task()
	newtask.taskname="demo"
	newtask.taskdesciption="demo"
	newtask.completed="demo"