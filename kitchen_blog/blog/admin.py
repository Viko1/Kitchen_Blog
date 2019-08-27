from django.contrib import admin
from .models import Post, Category

# Register your models here.
admin.site.register(Post)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)