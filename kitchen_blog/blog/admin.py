from django.contrib import admin
from .models import Post, Category

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'ingredients', 'body', 'post_image', 'category')
    prepopulated_fields = {'title': ('author', 'ingredients', 'body', )}
    search_fields = ['title', 'category__name', 'body', 'ingredients']


admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name__nome', 'slug__field1']


admin.site.register(Category, CategoryAdmin)