from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    post_list = Post.object.all()
    return render(request, 'blogapp/index.html', context={'post_list': post_list})


def index(request):
    return render(request, 'blogapp/index.html', context={
        'title': '博客首页',
        'welcome': '欢迎访问我的博客'
    })
