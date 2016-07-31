#! -*- encoding:utf-8 -*-
from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('category', 'is_markdown', 'title', 'text', 'markdown_text', 'tinymce_text')
        labels = {
            'category': '分类目录',
            'is_markdown': '是否保存为markdown文本',
            'title': '标题',
            'text': 'markdown文本',
            'markdown_text': 'markdown预览',
            'tinymce_text': 'tinymce文本',
        }
