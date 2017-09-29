from django.db import models
from django.contrib import admin

class Category(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 150)
    author = models.CharField(max_length=150)
    timestamp = models.DateTimeField()
    content = models.TextField()
    category = models.ForeignKey(Category, null=True, blank=True)

    def __str__(self):
        return self.title


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
