from django.shortcuts import render
from blog.models import Post, Category
from django.http import HttpResponse
from django.shortcuts import render_to_response
from el_pagination.decorators import page_template
# Create your views here.
@page_template('index_list.html')
def index(request, template = 'index.html', extra_context=None):
    count = {
        'post' : Post.objects.count(),
        'category' : Category.objects.count()
    }
    context = {
        'postList':Post.objects.order_by('-timestamp'),
        'count':count,
    }
    if extra_context is not None:
        context.update(extra_context)
    return render(request, template, context)





def post(request,time,id):
    post = Post.objects.get(id=id)
    tags = post.tags.all()
    count = {
        'post' : Post.objects.count(),
        'category' : Category.objects.count()
    }
    return render_to_response('post.html', { 'time':time, 'count' : count, 'post' : post, 'tags':tags })

@page_template('archives_list.html')
def archives(request, template = 'archives.html', extra_context = None):
    count = {
        'post' : Post.objects.count(),
        'category' : Category.objects.count()
    }
    posts = Post.objects.order_by('-timestamp')
    year = 0
    for post in posts:
        if post.timestamp.year == year:
            post.flag = 0
        else:
            post.flag = 1
        year = post.timestamp.year

    context = {
        'count' : count,
        'posts': posts,
    }
    if extra_context is not None:
        context.update(extra_context)
    return render(request,template, context)

@page_template('category_list.html')
def category(request,category_name,template = 'category.html', extra_context = None):

    category = Category.objects.get(name=category_name)
    posts = Post.objects.filter(category=category.id)
    count = {
        'post' : Post.objects.count(),
        'category' : Category.objects.count()
    }
    context = {
        'count' : count,
        'posts': posts,
        'category':category
    }
    if extra_context is not None:
        context.update(extra_context)
    return render(request, template, context)