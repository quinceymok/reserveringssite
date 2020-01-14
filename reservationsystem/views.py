from django.shortcuts import render
from.forms import CustomerForm

def index(request):
	return render(request, 'pages/index.html')


def appointment(request):
	return render(request, 'pages/appointment.html')

def bevestiging(request):
	form = CustomerForm(request.POST or None)
	if form.is_valid():
		form.save()
	context = {'form':form}
	return render(request, 'pages/bevestiging.html', context)

