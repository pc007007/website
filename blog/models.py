from django.db import models
from django.contrib import admin

class BlogsPost(models.Model):
    title = models.CharField(max_length = 150)
    content = models.TextField()
    timestamp = models.DateTimeField()
    author = models.CharField(max_length = 150)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')


admin.site.register(BlogsPost, BlogPostAdmin)

