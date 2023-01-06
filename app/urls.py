from django.urls import path

from .views import *

urlpatterns = [
	path('', index),
	path('professions/', profs),
	path('proffesions/<int:prof_id>/vostr/', prof_view_vostr),
	path('proffesions/<int:prof_id>/geo/', prof_view_geo),
	path('year/', years_view),
	path('year/<int:year>', skills_year_view)
]