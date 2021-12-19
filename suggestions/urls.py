from django.urls import path 
from . import views

urlpatterns = [
	path('suggest', views.suggest, name= 'suggest'),
	path('success', views.success, name= 'success'),
	path('suggestion_list', views.suggestion_list, name= 'suggestion_list')
]