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

def post(request,time,id):
    post = Post.objects.get(id=id)
    count = {
        'post' : Post.objects.count(),
        'category' : Category.objects.count()
    }
    return render_to_response('post.html', { 'time':time, 'count' : count, 'post' : post })