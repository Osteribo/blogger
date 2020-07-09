from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


posts = [
    {
        'author': 'Aaron0ster',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'

    },
    {
        'author': 'Aaron0ster',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'

    },
]

# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'   #  <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # orders the blogs newest to oldest
    ordering = ['-date_posted']
   


class PostDetailView(DetailView):
    model = Post
    





def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

