from django.shortcuts import render, get_object_or_404

from .models import Post

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
    return render(request, 'blogapp/detail.html', context={'post': post})

def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year, created_time__month=month)
    return render(request, 'blog/index.html', context={'post_list': post_list})

'''
def index(request):
    return render(request, 'blogapp/index.html', context={
        'title': '博客首页',
        'welcome': '欢迎访问我的博客'
    })
'''