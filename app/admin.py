from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
	pass


@admin.register(ProfessionDescriptionBlock)
class ProfessionDescriptionBlockAdmin(admin.ModelAdmin):
	pass


@admin.register(YearDiagram)
class YearDiagramAdmin(admin.ModelAdmin):
	pass


@admin.register(CitiesDiagram)
class CitiesDiagramAdmin(admin.ModelAdmin):
	pass


@admin.register(CitiesVacanciesDiagram)
class CitiesVacanciesDiagramAdmin(admin.ModelAdmin):
	pass


@admin.register(VacanciesDiagram)
class VacanciesDiagramAdmin(admin.ModelAdmin):
	pass


@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
	pass


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
	pass

