from django import template

from ..models import Post, Category

register = template.Library()    #实例化一个template.Library


@register.simple_tag    #函数装饰为register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all()[:num]

@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.all()