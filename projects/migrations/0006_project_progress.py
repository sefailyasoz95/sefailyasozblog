# Generated by Django 3.0.5 on 2020-05-04 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='progress',
            field=models.IntegerField(blank=True, default=0, verbose_name='İlerleme'),
        ),
    ]
