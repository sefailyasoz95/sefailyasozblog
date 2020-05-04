from django.contrib import admin

# Register your models here.
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'status']
    search_fields = ['name']
    list_per_page = 5
    readonly_fields = ('image_tag',)
    # prepopulated_fields = {'slug': ('title',)}


admin.site.register(Project, ProjectAdmin)