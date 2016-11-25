from django.shortcuts import render

from .models import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
	return HttpResponse('hello world')

def search(request):
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q'] # q is an object submitted by front
		return HttpResponse('you success')
	else:
		return HttpResponse('Please submit a search term')

def login(request):
	errors = []
	if 'name' in request.GET and request.GET['name']:
		if 'password' in request.GET and request.GET['password']:
			userName = request.GET['name']
			userPassword = request.GET['password']
			res = User.objects.filter(name = userName)
			if not res:
				errors.append('no such people')
			else:
				if res.password == userPassword:
					request.session['member_id'] = res.id
					return HttpResponseRedirect('/personInformation/?name=userName,password=userPassword')
		else:
			errors.append('please input your password')
	else:
		errors.append('please input your name')
	if (errors):
		return HttpResponseRedirect('/index/?errorMessage=errors')

def logout(request):
	try:
		del request.session['member_id']
	except KeyError:
		pass
	return HttpResponse("You're logged out")

	
