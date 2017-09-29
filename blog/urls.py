from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(\d{8})/(.+)' , views.post, name='post'),
    url(r'^archives/$',views.archives, name= 'archives')
]
