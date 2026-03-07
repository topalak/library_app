from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request=request, template_name='blog/home.html', context=context)
    #request is coming http request from the user's browser

def about(request):
    return render(request=request, template_name='blog/about.html', context={'title': 'About'})
# Create your views here.
