from django.shortcuts import render
from blog.models import Post, Category
from django.http import HttpResponse
from django.shortcuts import render_to_response
# Create your views here.
def index(request):
    #return HttpResponse("<h1>This is my blog homepage</h1>")
    postList = Post.objects.order_by('-timestamp')
    count = {
        'post' : Post.objects.count(),
        'category' : Category.objects.count()
    }
    return render_to_response('index.html', {'postList': postList, 'count' : count})

def post(request,time,title):
    blog_list = Post.objects.all()
    count = {
        'post' : Post.objects.count(),
        'category' : Category.objects.count()
    }
    return render_to_response('post.html', {'blog_list': blog_list, 'time':time, 'title':title, 'count' : count})