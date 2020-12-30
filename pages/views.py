from django.shortcuts import render
from .models import Team
from cars.models import car

# Create your views here.
def home(request):
	teams = Team.objects.all()
	featured_cars = car.objects.order_by('-created_date').filter(isfeatured=True)
	latest_cars = car.objects.order_by('-created_date').all()
	data = {
		'teams': teams,
		'featured_cars': featured_cars,
		'latest_cars': latest_cars,
	}

	return render(request, 'pages/home.html', data)

def about(request):
	teams = Team.objects.all()
	data = {
		'teams': teams,
	}
	return render(request, 'pages/about.html', data)

def contact(request):
	return render(request, 'pages/contact.html')

def services(request):
	return render(request, 'pages/services.html')
