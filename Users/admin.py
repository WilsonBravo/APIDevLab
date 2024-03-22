from django import forms
from django.contrib import admin
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        } 

class UserAdmin(admin.ModelAdmin):
    form = UserForm
    search_fields = ('firstName',)
    list_display = [field.name for field in User._meta.get_fields()]
    list_per_page = 20 

admin.site.register(User, UserAdmin)
