from django.shortcuts import render
from .models import BlogPost


# Create your views here.


def index(request):
    # blog_post = BlogPost.objects.get(pk=6)
    blog_post = BlogPost.objects.all()

    return render(request, 'blog/index.html', context={'blog_post': blog_post})


def article(request, slug):
    post = BlogPost.objects.get(slug=slug)
    return render(request, "blog/article.html", context={'post': post})
