from django.shortcuts import render

from .models import *
from django.http import HttpResponse
# Create your views here.
def index(request):
	return HttpResponse('hello world')

def search(request):
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q'] # q is an object submitted by front
	else:
		return HttpResponse('Please submit a search term')