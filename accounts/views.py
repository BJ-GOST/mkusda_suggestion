from django.shortcuts import render, redirect
from .forms import *
from django.contrib import auth, messages
from django.http import Http404



# Create your views here.

def landing(request):
	return render(request, 'landing.html' )


def createuser(request):
	form = CreateUser()
	if request.method == 'POST':
		form=CreateUser(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	return render(request, 'create.html', {'form':form})


def login(request):
	if request.user.is_authenticated:
		return redirect ('suggest')
	
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		print(password, username)
		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			return redirect('suggest')
		else:
			messages.error(request, 'wrong username or password')
	
	return render(request, 'login.html')


def logout(request):
	auth.logout(request)
	return render(request, 'logout.html')
