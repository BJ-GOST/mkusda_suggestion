from django.urls import path
from . import views

urlpatterns = [
	path('landing', views.landing, name= 'landing'),
	path('createuser', views.createuser, name= 'createuser'),
	path('login', views.login, name= 'login'),
	path('logout', views.logout, name= 'logout')
]