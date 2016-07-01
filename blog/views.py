# encoding=utf8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from .forms import PostForm
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from haystack.forms import SearchForm
from django.http import HttpResponse, HttpResponseRedirect
from PIL import Image
#python3.4 强制encoding utf8，所以不需要下面两句
#import sys
#reload(sys)
#sys.setdefaultencoding( "utf-8" )

def full_search(request):
    """全局搜索"""
    keywords = request.GET['q']
    sform = SearchForm(request.GET)
    posts = sform.search()
    return render(request, 'blog/post_search_list.html',
                  {'posts': posts, 'list_header': '关键字 \'{}\' 搜索结果'.format(keywords)})

@login_required
def add_category(request):
    cate_name = request.GET.get('category_name')
    url_name = request.GET.get('current_url')
    category = Category.objects.create(name=cate_name)
    return HttpResponseRedirect(url_name)

# Create your views here.

def post_detail(request, pk):
    print 'ttt'
    post = get_object_or_404(Post, pk=pk)
    post.text = post.text.replace('[!--more--]', '', 1)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_list(request):
    """所有已发布文章"""
    postsAll = Post.objects.annotate(num_comment=Count('id')).filter(
        published_date__isnull=False).prefetch_related('category').order_by('-published_date')
    paginator = Paginator(postsAll, 5)  # Show 5 contacts per page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post_list.html', {'posts': posts, 'page': True})

def post_list_by_category(request, cg):
    """根据目录列表已发布文章"""
    posts = Post.objects.filter(
        published_date__isnull=False, category__name=cg).prefetch_related(
        'category').order_by('-published_date')
    return render(request, 'blog/post_list.html',
                  {'posts': posts, 'list_header': '\'{}\' 分类的存档'.format(cg)})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog.views.post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog.views.post_list')

@login_required
def upload(request):
    try:
        file = request.FILES['image']
        #form提交的文件的名字，上面html里面的name
        img = Image.open(file)
        img.thumbnail((500, 500), Image.ANTIALIAS)
        img.save('static/upload/images/'+file.name, img.format)
        #图片的name和format都是动态获取的，支持png，jpeg，gif等
    except Exception as e:
        return HttpResponse('error %s' % e)
    path = '/site_media/'+file.name
    return HttpResponse("<script>top.$('.mce-btn.mce-open').parent().find('.mce-textbox').val('%s').closest('.mce-window').find('.mce-primary').click();</script>" % path)

def about_me(request):
    return render(request, 'blog/about_me.html', {})
