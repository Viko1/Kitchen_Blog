from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



#Category
class Category(models.Model):

    name = models.CharField(max_length=240, blank=True, null=True, default='Category')
    slug = models.SlugField(max_length=240, unique=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name






STATUS = (
    (0,"Draft"),
    (1,"Publish")
)




#Post
class Post(models.Model):

    title = models.CharField(max_length=255, blank=True, null=True, default='Post')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients = models.TextField(default='ingredients')
    body = models.TextField()
    post_image = models.ImageField(upload_to='blog_images', default='post_image')
    image = models.ImageField(upload_to='blog_images')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        ordering = ['-created_on']

