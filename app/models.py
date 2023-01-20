import base64

from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Profession(models.Model):
	name = models.CharField(verbose_name='Название профессии', max_length=128)
	is_visible = models.BooleanField(verbose_name='Видно на сайте?', default=True)

	def __str__(self):
		return f'Профессия: {self.name}'

	class Meta:
		verbose_name = 'Профессия'
		verbose_name_plural = 'Профессии'
		db_table = 'professions'


class ProfessionDescriptionBlock(models.Model):
	profession = models.ForeignKey(verbose_name='Профессия', to='app.Profession', on_delete=models.CASCADE, null=True, default=None)
	title = models.CharField(verbose_name='Заголовок описания', max_length=500, default='Заголовок')
	description = RichTextField(verbose_name='Текст описания', default='Без описания')

	def __str__(self):
		if self.profession:
			return f'Описание для профессии {self.profession.name}'
		return 'Описание для профессии (Не привязано)'

	class Meta:
		verbose_name = 'Описание профессии'
		verbose_name_plural = 'Описание профессий'
		db_table = 'profession_descriptions'


class YearDiagram(models.Model):
	profession = models.ForeignKey(verbose_name='Профессия', to='app.Profession', on_delete=models.CASCADE)
	diagram_title = models.CharField(verbose_name='Заголовок диаграммы', max_length=200, default='Заголовок диаграммы')
	image = models.BinaryField(verbose_name='Картинка в бинарном виде', null=True, default=None)
	image_raw = models.ImageField(verbose_name='Картинка в чистом виде', upload_to='cache/')

	def save(self, *args, **kwargs):
		if self.image_raw:
			try:
				img_file = self.image_raw.open('rb')
				self.image = img_file.read()
			except:
				pass
		super(YearDiagram, self).save(*args, **kwargs)

	def __str__(self):
		return f'Годовая диаграмма для профессии {self.profession.name}'

	class Meta:
		verbose_name = 'Годовая диаграмма'
		verbose_name_plural = 'Годовые диаграммы'
		db_table = 'year_diagrams'


class CitiesDiagram(models.Model):
	profession = models.ForeignKey(verbose_name='Профессия', to='app.Profession', on_delete=models.CASCADE)
	diagram_title = models.CharField(verbose_name='Заголовок диаграммы', max_length=200, default='Заголовок диаграммы')
	image = models.BinaryField(verbose_name='Картинка в бинарном виде', null=True, default=None)
	image_raw = models.ImageField(verbose_name='Картинка в чистом виде', upload_to='cache/')

	def save(self, *args, **kwargs):
		if self.image_raw:
			try:
				img_file = self.image_raw.open('rb')
				self.image = img_file.read()
			except:
				pass
		super(CitiesDiagram, self).save(*args, **kwargs)

	def __str__(self):
		return f'Диаграмма по городам для профессии {self.profession.name}'

	class Meta:
		verbose_name = 'Диаграмма по городам'
		verbose_name_plural = 'Диаграммы по городам'
		db_table = 'city_diagrams'


class CitiesVacanciesDiagram(models.Model):
	profession = models.ForeignKey(verbose_name='Профессия', to='app.Profession', on_delete=models.CASCADE)
	diagram_title = models.CharField(verbose_name='Заголовок диаграммы', max_length=200, default='Заголовок диаграммы')
	image = models.BinaryField(verbose_name='Картинка в бинарном виде', null=True, default=None)
	image_raw = models.ImageField(verbose_name='Картинка в чистом виде', upload_to='cache/')

	def save(self, *args, **kwargs):
		if self.image_raw:
			try:
				img_file = self.image_raw.open('rb')
				self.image = img_file.read()
			except:
				pass
		super(CitiesVacanciesDiagram, self).save(*args, **kwargs)

	def __str__(self):
		return f'Диаграмма ваканский по городам для профессии {self.profession.name}'

	class Meta:
		verbose_name = 'Диаграмма ваканский по городам'
		verbose_name_plural = 'Диаграммы ваканский по городам'
		db_table = 'city_vacancy_diagrams'


class VacanciesDiagram(models.Model):
	profession = models.ForeignKey(verbose_name='Профессия', to='app.Profession', on_delete=models.CASCADE)
	diagram_title = models.CharField(verbose_name='Заголовок диаграммы', max_length=200, default='Заголовок диаграммы')
	image = models.BinaryField(verbose_name='Картинка в бинарном виде', null=True, default=None)
	image_raw = models.ImageField(verbose_name='Картинка в чистом виде', upload_to='cache/')

	def save(self, *args, **kwargs):
		if self.image_raw:
			try:
				img_file = self.image_raw.open('rb')
				self.image = img_file.read()
			except:
				pass
		super(VacanciesDiagram, self).save(*args, **kwargs)

	def __str__(self):
		return f'Диаграмма вакансий для профессии {self.profession.name}'

	class Meta:
		verbose_name = 'Диаграмма вакансий'
		verbose_name_plural = 'Диаграммы вакансий'
		db_table = 'vacancy_diagrams'


class Year(models.Model):
	profession = models.ForeignKey(verbose_name='Профессия', to='app.Profession', on_delete=models.CASCADE)
	year = models.IntegerField(verbose_name='Год')
	is_visible = models.BooleanField(verbose_name='Видно на сайте?', default=True)

	def __str__(self):
		return f'Профессия: {self.profession.name} - {self.year} год'

	class Meta:
		verbose_name = 'Год'
		verbose_name_plural = 'Года'
		db_table = 'skill_years'


class Skill(models.Model):
	name = models.CharField(verbose_name='Название навыка', max_length=50)
	weight = models.DecimalField(verbose_name='Востребованность', decimal_places=2, max_digits=5)
	year = models.ForeignKey(verbose_name='Год навыка', to='app.Year', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.name} - навык профессии {self.year.profession.name} {self.year.year} года'

	class Meta:
		verbose_name = 'Навык года'
		verbose_name_plural = 'Навыки года'
		db_table = 'skills'
