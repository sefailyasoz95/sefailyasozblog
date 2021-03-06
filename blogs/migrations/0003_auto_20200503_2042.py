# Generated by Django 3.0.5 on 2020-05-03 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20200503_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='status',
            field=models.CharField(blank=True, choices=[('Yayında', 'Yayında'), ('Yeni', 'Yeni'), ('Kaldırıldı', 'Kaldırıldı')], default='Yeni', max_length=15),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog',
            field=models.TextField(blank=True, verbose_name='Blog İçeriği'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.CharField(max_length=50, verbose_name='Fotoğraf'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='rate',
            field=models.IntegerField(blank=True, verbose_name='Değerlendirme'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='readings',
            field=models.IntegerField(blank=True, verbose_name='Okunma Sayısı'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Başlık'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi'),
        ),
    ]
