from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import Post

# Create your views here.

# def indexView(request):
#     return render(request, 'base.html')

class IndexView(ListView):
    model = Post
    template_name = 'index.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class CreatePostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'




