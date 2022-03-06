from django.contrib import admin
from Blog.models import Post, BlogComment

admin.site.register(BlogComment)
admin.site.register(Post)