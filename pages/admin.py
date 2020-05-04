from django.contrib import admin

# Register your models here.
from .models import Setting, ContactFormMessage


class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email', 'subject', 'message', 'note', 'status']
    list_filter = ['status']


class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'address', 'email', 'image_tag', 'status']
    search_fields = ['name']
    list_per_page = 5
    readonly_fields = ('image_tag',)
    #prepopulated_fields = {'slug': ('title',)}

admin.site.register(ContactFormMessage, ContactFormMessageAdmin)
admin.site.register(Setting, SettingAdmin)

'''
<label for="email">Email </label>
                <input type="email" class="form-control border-secondary" id="email" placeholder="Your email here">
                <small class="text-muted form-text">Your email will not ever be shared</small>
                <label for="subject" class="mt-2">Subject </label>
                <input type="text" class="form-control border-secondary" id="subject" placeholder="Subject here...">
                <label for="message" class="mt-2 border-secondary">Message </label>
                <textarea class="form-control border-secondary" id="message" rows="3"> </textarea>
'''