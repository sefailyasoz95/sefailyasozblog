# Generated by Django 3.0.5 on 2020-05-04 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20200505_0210'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='language',
            field=models.CharField(blank=True, max_length=250, verbose_name='Kodlanma Dili'),
        ),
    ]