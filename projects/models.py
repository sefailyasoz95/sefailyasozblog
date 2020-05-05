from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.safestring import mark_safe

class Project(models.Model):
    STATUS = (
        ('Yayında', 'Yayında'),
        ('Yeni', 'Yeni'),
        ('Kaldırıldı', 'Kaldırıldı'),
    )
    title = models.CharField(blank=True, max_length=250, verbose_name="Proje Başlığı")
    detail = RichTextField()
    description = models.CharField(blank=True, max_length=250, verbose_name="Proje Özet")
    link = models.CharField(blank=True, max_length=250, verbose_name="Proje Linki")
    language = models.CharField(blank=True, max_length=250, verbose_name="Kodlanma Dili")
    image = models.ImageField(blank=True, upload_to='', verbose_name="Fotoğraf")
    rate = models.IntegerField(blank=True, verbose_name="Değerlendirme", default=0)
    progress = models.IntegerField(blank=True, verbose_name="İlerleme", default=0)
    status = models.CharField(blank=True, choices=STATUS, default='Yeni', max_length=15)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Güncellenme Tarihi")
    slug = models.SlugField(blank=True, default="")

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50" />'.format(self.image.url))

    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})


class Language(models.Model):
    STATUS = (
        ('Yayında', 'Yayında'),
        ('Yeni', 'Yeni'),
        ('Kaldırıldı', 'Kaldırıldı'),
    )
    name = models.CharField(blank=True, max_length=250, verbose_name="Dil")
    progress = models.IntegerField(blank=True, verbose_name="İlerleme", default=0)
    numberofprojects = models.IntegerField(blank=True, verbose_name="Yapılan Proje Sayısı", default=0)
    status = models.CharField(blank=True, choices=STATUS, default='Yeni', max_length=15)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Güncellenme Tarihi")

    def __str__(self):
        return self.name