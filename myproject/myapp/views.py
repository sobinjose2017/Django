from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.template import Template
from django.shortcuts import render
from .import views
from myapp.models import *
from django.http import JsonResponse
def index(request):
	template = loader.get_template('index.html')
	context={"title":"Add Task"}
	return HttpResponse(template.render(context, request))
def add(request):
	template = loader.get_template('addtask.html')
	context={"title":"Add Task","heading":"Add Task"}
	return HttpResponse(template.render(context, request))
def create(request):
	if request.method=='POST':
		name = request.POST['name']
		taskdes = request.POST['taskdes']
		completed = request.POST['completed']
		newtask=task()
		newtask.taskname=name
		newtask.taskdesciption=taskdes
		newtask.complete=completed
		result=newtask.save()
		print (result)
		template = loader.get_template('view.html')
		context={"Msg":"Registration Successful"}
		return HttpResponseRedirect("/myapp/view/")
		# if result==true:
		# 	template = loader.get_template('view.html')
		# 	context={"Msg":"Registration Successful"}
		# 	return HttpResponse(template.render(context, request))
		# else:
		# 	template = loader.get_template('addtask.html')
		# 	context={"Msg":"Error"}
		# 	return HttpResponse(template.render(context, request))
	else:
		template = loader.get_template('addtask.html')
		context={"Msg":"Method Not Found"}
		return HttpResponse(template.render(context, request))
def view(request):
	result = task.objects.all()
	template = loader.get_template('view.html')
	context={'all_users':result}
	return HttpResponse(template.render(context, request))
def edit(request):
	if request.method=='GET':
		task_id=request.GET['id']
		result = task.objects.get(id=task_id)
		template = loader.get_template('edit.html')
		context={'taskname':result.taskname,'descrtioion':result.taskdesciption,'completed':result.complete,'id':task_id}
		return HttpResponse(template.render(context, request))
	else:
		template = loader.get_template('addtask.html')
		context={"title":"Add Task","heading":"Add Task"}
		return HttpResponse(template.render(context, request))

def delete(request):
	if request.method=='GET':
		task_id=request.GET['id']
		result = task.objects.get(id=task_id).delete()
		return HttpResponseRedirect("/myapp/view/")
	
def update(request):
	if request.method=='POST':
		task_id=request.POST['id']
		name = request.POST['name']
		taskdes = request.POST['taskdes']
		completed = request.POST['completed']
		result = task.objects.filter(id=task_id).update(taskname=name,taskdesciption=taskdes,complete=completed)
		return HttpResponseRedirect("/myapp/view/")
		
         
 
