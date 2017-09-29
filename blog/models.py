from django.db import models
from django.contrib import admin

class BlogsPost(models.Model):
    title = models.CharField(max_length = 150)
    author = models.CharField(max_length=150)
    timestamp = models.DateTimeField()
    content = models.TextField()
    category =models.CharField(max_length = 150)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')


admin.site.register(BlogsPost, BlogPostAdmin)

