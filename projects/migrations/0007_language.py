# Generated by Django 3.0.5 on 2020-05-05 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_progress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, verbose_name='Dil')),
                ('progress', models.IntegerField(blank=True, default=0, verbose_name='İlerleme')),
                ('numberofprojects', models.IntegerField(blank=True, default=0, verbose_name='Yapılan Proje Sayısı')),
                ('status', models.CharField(blank=True, choices=[('Yayında', 'Yayında'), ('Yeni', 'Yeni'), ('Kaldırıldı', 'Kaldırıldı')], default='Yeni', max_length=15)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
            ],
        ),
    ]
