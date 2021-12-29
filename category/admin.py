from django.contrib import admin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('categoy_name',)}
    list_display = ('categoy_name', 'slug')

admin.site.register(Category, CategoryAdmin)