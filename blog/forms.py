#! -*- encoding:utf-8 -*-
from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('category', 'title', 'text')
        labels = {
            'category': '分类目录',
            'text': '正文',
            'title': '标题',
        }
