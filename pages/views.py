from django.shortcuts import render
from .models import Team
from cars.models import car

# Create your views here.
def home(request):
	teams = Team.objects.all()
	featured_cars = car.objects.order_by('-created_date').filter(isfeatured=True)
	latest_cars = car.objects.order_by('-created_date').all()
	# search_field = car.objects.values('model','city','year','body_style')
	model_search = car.objects.values_list('model',flat=True).distinct()
	city_search = car.objects.values_list('city',flat=True).distinct()
	body_style_search = car.objects.values_list('body_style',flat=True).distinct()
	year_search = car.objects.values_list('year',flat=True).distinct()
	data = {
		'teams': teams,
		'featured_cars': featured_cars,
		'latest_cars': latest_cars,
		'model_search':model_search,
		'year_search':year_search,
		'body_style_search':body_style_search,
		'city_search':city_search,
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
