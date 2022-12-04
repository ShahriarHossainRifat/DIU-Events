from django.http import HttpResponse
from django.shortcuts import render

from blogs.models import Post


# Create your views here.

def home(request):
    # load all the posts from db(10)
    posts = Post.objects.all()[:11]
    # print(posts)
    data = {
        'posts': posts
    }
    return render(request, 'home.html', data)


def post(request, url):
    post = Post.objects.get(url=url)
    print(post)
    return render(request, 'post.html', {'post': post})
