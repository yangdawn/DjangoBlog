import markdown
from django.shortcuts import render, get_object_or_404
form .models import posixpath


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.condehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'blogapp/detail.html', context={'post': post})