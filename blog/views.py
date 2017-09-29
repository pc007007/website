from django.shortcuts import render
from blog.models import BlogsPost
from django.http import HttpResponse
from django.shortcuts import render_to_response
# Create your views here.
def index(request):
    #return HttpResponse("<h1>This is my blog homepage</h1>")
    blog_list = BlogsPost.objects.all()
    return render_to_response('index.html', {'blog_list': blog_list})

def post(request,time,title):
    blog_list = BlogsPost.objects.all()
    return render_to_response('post.html', {'blog_list': blog_list,'time':time,'title':title})