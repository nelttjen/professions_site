from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from .models import *


NO_IMAGE_LINK = 'media/default/no_image.png'


# Create your views here.
def index(request):
	return render(request, 'app/index.html')


def profs(request):
	profession_list = Profession.objects.filter(is_visible=True).all().values_list('id', 'name', named=True)
	payload = {
		'profs': profession_list
	}
	return render(request, 'app/prof.html', payload)


def prof_overview(request, prof_id):
	profession = Profession.objects.filter(id=prof_id).first()
	if not profession:
		return HttpResponseNotFound()
	prof_descriptions = profession.description_blocks.all().values_list('title', 'description', named=True)
	payload = {
		'prof': profession,
		'prof_descs': prof_descriptions
	}
	return render(request, 'app/prof_detail_overview.html', payload)


def prof_view_vostr(request, prof_id):
	profession = Profession.objects.filter(id=prof_id).first()
	if not profession:
		return HttpResponseNotFound()
	year_diagram = YearDiagram.objects.filter(profession=profession).first()
	vacancies_diagram = VacanciesDiagram.objects.filter(profession=profession).first()
	if year_diagram:
		link = f'media/year_diagram/{year_diagram.id}.jpg'
		try:
			with open(link, 'wb') as file:
				file.write(year_diagram.image)
		except:
			link = NO_IMAGE_LINK
		year_diagram = {
			'title': year_diagram.diagram_title,
			'image': '/' + link
		}
	else:
		year_diagram = {
			'title': 'Диаграмма зарплат по годам не добавлена',
			'image': '/' + NO_IMAGE_LINK
		}
	if vacancies_diagram:
		link = f'media/vacancies_diagram/{vacancies_diagram.id}.jpg'
		try:
			with open(link, 'wb') as file:
				file.write(vacancies_diagram.image)
		except:
			link = NO_IMAGE_LINK
		vacancies_diagram = {
			'title': vacancies_diagram.diagram_title,
			'image': '/' + link
		}
	else:
		vacancies_diagram = {
			'title': 'Диаграмма количества вакансий по годам не добавлена',
			'image': '/' + NO_IMAGE_LINK
		}
	payload = {
		'prof': profession,
		'diag_1': year_diagram,
		'diag_2': vacancies_diagram,
	}
	return render(request, 'app/prof_detail_diagram.html', payload)


def prof_view_geo(request, prof_id):
	profession = Profession.objects.filter(id=prof_id).first()
	if not profession:
		return HttpResponseNotFound()
	cities_diagram = CitiesDiagram.objects.filter(profession=profession).first()
	cities_vacancies_diagram = CitiesVacanciesDiagram.objects.filter(profession=profession).first()
	if cities_diagram:
		link = f'media/year_diagram/{cities_diagram.id}.jpg'
		try:
			with open(link, 'wb') as file:
				file.write(cities_diagram.image)
		except:
			link = NO_IMAGE_LINK
		cities_diagram = {
			'title': cities_diagram.diagram_title,
			'image': '/' + link
		}
	else:
		cities_diagram = {
			'title': 'Диаграмма зарплат по городам не добавлена',
			'image': '/' + NO_IMAGE_LINK
		}
	if cities_vacancies_diagram:
		link = f'media/vacancies_diagram/{cities_vacancies_diagram.id}.jpg'
		try:
			with open(link, 'wb') as file:
				file.write(cities_vacancies_diagram.image)
		except:
			link = NO_IMAGE_LINK
		cities_vacancies_diagram = {
			'title': cities_vacancies_diagram.diagram_title,
			'image': '/' + link
		}
	else:
		cities_vacancies_diagram = {
			'title': 'Диаграмма количества вакансий по городам не добавлена',
			'image': '/' + NO_IMAGE_LINK
		}
	payload = {
		'prof': profession,
		'diag_1': cities_diagram,
		'diag_2': cities_vacancies_diagram,
	}
	return render(request, 'app/prof_detail_diagram.html', payload)


def years_view(request):
	pass


def skills_year_view(request, year):
	pass