from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post, Category
from django.urls import reverse_lazy



# Create your views here.

# def indexView(request):
#     return render(request, 'base.html')


class PostCategory(ListView):
    model = Post
    template_name = 'list_by_category.html'
    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Post.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(PostCategory, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context

class IndexView(ListView):

    model = Post
    template_name = 'index.html'
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    paginate_by = 4
    # query = request.GET.get

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class CreatePostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'


class PostEditView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = '__all__'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')