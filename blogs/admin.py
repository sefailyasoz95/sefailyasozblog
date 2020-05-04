from django.contrib import admin

from .models import Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'readings', 'image_tag', 'status', 'created_date', 'updated_date']
    search_fields = ['name']
    list_per_page = 5
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog,BlogAdmin)