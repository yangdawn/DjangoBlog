from django.shortcuts import render, get_object_or_404, redirect
from blogapp.models import Post

from .models import Comment 
from .forms import CommentForm

def post_comment(request, post_pk):
    #评论需与被评论的文章关联起来，
    #使用django提供的函数get_object_or_404获取被评论的文章。
    post = get_object_or_404(Post, pk=post_pk)

    #http请求有get和post，一般表单提交数据都是通过post请求，
    #因此把请求限定为post时才处理表单数据。
    if request.method == "POST":
        form = commentForm(request.POST)    #利用用户提交的数据构成class实例CommentForm。

    if form.is_valid():
        #检查数据是合法则调用表单的save方法保存数据到数据库。
        #commit=False的作用仅仅是利用表单的数据生成Comment模型类的实例，但不保存数据。
        comment = form.save(commit=False)
        comment.post = post    #关联评论和被评论的文章。
        comment.save()    #调用模型实例save方法将评论数据保存到数据库。
        return redirect(post) #重定向到post的详情页。

    else:
        #监测数据是否合法，否则渲染详情页，并且渲染表单错误。
        #因次将三个模版变量传给detial.html，post,form(表单)和comment_list(评论列表)。
        #post.comment_set.all()方法类似与Post.objects.all(),
        #其作用是获取文章post下的全部评论。
        #因为post和Comment是ForeignKey关联，因此使用post.comment_set.all()反向查询全部评论。
        #正向查询是comment.post。
        comment_list = post.comment_set.all()
        context = {'post': post,
                   'form': form,
                   'comment_list': comment_list
                   }
        return render(request, 'blogapp/detail.html', context=context)
    #不是post请求，说明用户没有提交表单，则重定向到文章详情页。
    return redirect(post)    