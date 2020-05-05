from django.contrib import admin

# Register your models here.
from .models import Project, Language


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'status']
    search_fields = ['name']
    list_per_page = 5
    readonly_fields = ('image_tag',)
    # prepopulated_fields = {'slug': ('title',)}


class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'progress', 'numberofprojects', 'status']
    search_fields = ['name']
    list_per_page = 5


admin.site.register(Language, LanguageAdmin)
admin.site.register(Project, ProjectAdmin)