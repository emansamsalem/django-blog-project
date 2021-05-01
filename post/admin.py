from django.contrib import admin

# Register your models here.

# class name ---> added
from .models import Post


admin.site.register(Post)