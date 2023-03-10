# Generated by Django 4.1.5 on 2023-01-07 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_year_is_visible'),
    ]

    operations = [
        migrations.AddField(
            model_name='year',
            name='profession',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.profession', verbose_name='Профессия'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='year',
            name='year',
            field=models.IntegerField(verbose_name='Год'),
        ),
    ]
