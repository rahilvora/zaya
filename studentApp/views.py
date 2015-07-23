from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return render(request,'index.html')
	#return HttpResponse("Hello, world. You're at the polls index.")
def addStudent(request):
	return render(request,'addStudent.html')

def behaviour(request):
	return render(request,'behaviour.html')

def add(self):
	return HttpResponse("Data Added")

