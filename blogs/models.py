from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.safestring import mark_safe


class Blog(models.Model):
    STATUS = (
        ('Yayında', 'Yayında'),
        ('Yeni', 'Yeni'),
        ('Kaldırıldı', 'Kaldırıldı'),
    )
    title = models.CharField(blank=True, max_length=100, verbose_name="Başlık")
    blog = RichTextField(blank=True, verbose_name="Blog İçeriği")
    description = models.TextField(blank=True, verbose_name="Blog Özet", default=" ")
    image = models.ImageField(blank=True, upload_to='', verbose_name="Fotoğraf")
    readings = models.IntegerField(blank=True, verbose_name="Okunma Sayısı", default=0)
    rate = models.IntegerField(blank=True, verbose_name="Değerlendirme", default=0)
    status = models.CharField(blank=True, choices=STATUS, default='Yeni', max_length=15)
    slug = models.SlugField(blank=True, default="")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Güncellenme Tarihi")

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50" />'.format(self.image.url))

    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('blog_blog', kwargs={'slug': self.slug})
