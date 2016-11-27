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
					return HttpResponseRedirect('/index/?errorMessage=errors')
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

<<<<<<< HEAD
def register(request):
	errors = []
	if request.method == 'POST':
		if not request.POST.get('name', ''):
			errors.append('Enter a name')
		if not request.POST.get('gender', ''):
			errors.append('Enter a gender')
		if not request.POST.get('idNum', ''):
			errors.append('Enter an idNum')
		if not request.POST.get('birthdate',''):
			errors.append('Enter a birthdate')
		if not request.POST.get('password', ''):
			errors.append('Enter a password')
		if not request.POST.get('phoneNum', ''):
			errors.append('Enter a phoneNum')
		if not errors:
			name = request.POST['name']
			password = request.POST['password']
			sex = request.POST['gender']
			birthDate = request.POST['birthdate']
			idNum = request.POST['idNum']
			phoneNum = request.PSOT['phoneNum']
			user_tmp = User(name = name, password = password, sex = sex, birthday = birthDate, telephone = phoneNum, idCard = idNum)
			user_tmp.save();

			res = User.objects.filter(name = name)
			request.session['member_id'] = res.id
	# return where? i think it should be discussed
	return HttpResponseRedirect('/index/?errorMessage=errors')
=======
>>>>>>> 55558ac7c18e54d41e0e33ddd0049486782cbdf6
	
