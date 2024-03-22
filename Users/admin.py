from django.contrib import admin
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class customFieldsInline(admin.StackedInline):
    model  = customFields
    can_delete = False
    verbose_name = 'Additional info'
    verbose_name_plural = 'Additional info'

class customizedUserAdmin(UserAdmin):
    inlines = (customFieldsInline,)

admin.site.unregister(User)
admin.site.register(User, customizedUserAdmin)

# from django.contrib import admin
# from .models import *

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'
#         widgets = {
#             'password': forms.PasswordInput(render_value=True),
#         } 

# class UserAdmin(admin.ModelAdmin):
#     form = UserForm
#     search_fields = ('firstName',)
#     list_display = [field.name for field in User._meta.get_fields()]
#     list_per_page = 20 

# admin.site.register(User, UserAdmin)
