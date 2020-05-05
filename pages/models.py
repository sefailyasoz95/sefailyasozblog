from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class Setting(models.Model):
    STATUS = (
        ('TRUE', 'EVET'),
        ('FALSE', 'HAYIR'),
    )
    title = models.CharField(blank=True, max_length=150, verbose_name="Site Adı")
    keywords = models.CharField(blank=True, max_length=100)
    description = models.CharField(blank=True, max_length=100)
    company = models.CharField(blank=True, max_length=100, verbose_name="Şirket Adı")
    address = models.CharField(blank=True, max_length=200, verbose_name="Adres")
    phone = models.CharField(blank=True, max_length=15, verbose_name="Telefon")
    fax = models.CharField(blank=True, max_length=15, verbose_name="Fax")
    email = models.CharField(blank=True, max_length=100, verbose_name="Email")
    smtpserver = models.CharField(blank=True, max_length=100)
    smtpemail = models.CharField(blank=True, max_length=100)
    smtppassword = models.CharField(blank=True, max_length=100)
    smtpport = models.CharField(blank=True, max_length=10)
    icon = models.ImageField(blank=True, upload_to='',verbose_name="Logo")
    facebook = models.CharField(blank=True, max_length=100)
    twitter = models.CharField(blank=True, max_length=100)
    instagram = models.CharField(blank=True, max_length=100)
    youtube = models.CharField(blank=True, max_length=100, default="")
    github = models.CharField(blank=True, max_length=100, default="")
    kariyer = models.CharField(blank=True, max_length=100, default="")
    aboutme = RichTextField()
    contact = RichTextField()
    career = RichTextField()
    welcoming = RichTextField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50" />'.format(self.icon.url))

    image_tag.short_description = 'Logo'


class ContactFormMessage(models.Model):
    STATUS = (
        ('Yeni', 'Yeni'),
        ('Okundu', 'Okundu'),
        ('Cevaplandı', 'Cevaplandı')
    )
    name = models.CharField(blank=False, max_length=50)
    surname = models.CharField(blank=False, max_length=50)
    email = models.CharField(blank=False, max_length=150)
    subject = models.CharField(blank=False, max_length=150)
    message = models.CharField(blank=False, max_length=255)
    ip = models.CharField(blank=False, max_length=150)
    note = models.CharField(blank=True, max_length=150)
    status = models.CharField(max_length=10, choices=STATUS, default='Yeni')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name