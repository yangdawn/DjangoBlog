from django.shortcuts import render, get_object_or_404

from .models import Post, Category
from comments.forms import CommentForm

import markdown


def index(request):
    post_list = Post.objects.all()
    return render(request, 'blogapp/index.html', context={'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    #文章详情页评论视图。                              
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'blogapp/detail.html', context=context)
    

def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year, created_time__month=month)
    return render(request, 'blogapp/index.html', context={'post_list': post_list})

def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request, 'blogapp/index.html', context={'post_list': post_list})

'''
def index(request):
    return render(request, 'blogapp/index.html', context={
        'title': '博客首页',
        'welcome': '欢迎访问我的博客'
    })
'''