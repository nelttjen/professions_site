from django.shortcuts import render


# Create your views here.
def index(request):
	return render(request, 'app/index.html')


def profs(request):
	pass


def prof_view_vostr(request, prof_id):
	pass


def prof_view_geo(request, prof_id):
	pass


def years_view(request):
	pass


def skills_year_view(request, year):
	pass