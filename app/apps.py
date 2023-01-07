import os

from django.apps import AppConfig as Appcfg


class AppConfig(Appcfg):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        roots = (
            'media/',
            'media/cache/',
            'media/cities_diagram/',
            'media/cities_vacancies_diagram/',
            'media/vacancies_diagram/',
            'media/year_diagram/',
        )
        for root in roots:
            os.mkdir(root) if not os.path.exists(root) else None