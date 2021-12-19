from django.shortcuts import render, redirect
from .forms import suggestionform
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .models import suggestion

# Create your views here.
#“ No amount of guilt can solve the past, and no amount of anxiety can change the future. ”


@login_required(login_url='login')
def suggest(request):
	form = suggestionform()
	if request.method == 'POST':
		form = suggestionform(request.POST)
		if form.is_valid():
			suggestion = form.save(commit=False)
			suggestion.author = request.user;
			suggestion.save(suggestion.author)
			return redirect('success')

			subject = 'Thank you for your suggestion, God bless you'
			message = f'Dear {suggestion.author} we Thank you for your suggestion and promise to consider it'
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [request.user.email]
			send_mail(subject, message, email_from, recipient_list)
	return render(request, 'suggest.html', {'form':form})


def suggestion_list(request):
	suggestions =suggestion.objects.all()
	context={
		'suggestions':suggestions
	}
	return render (request, 'suggestion_list.html', context)



def success(request):
	return render(request, 'success.html')

