#! -*- encoding:utf-8 -*-
from django.contrib import admin

# Register your models here.
from .models import Post

admin.site.register(Post)
