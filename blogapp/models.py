from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse



class Category(models.Model):    #分类。django要求继承model.Model类。
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):    #标签。继承models.Model类。
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):    #文章数据库表
    title = models.CharField(max_length=70)    #文章标题。
    body = models.TextField()    #文章主体。
    created_time =  models.DateTimeField()    #文章创建时间。
    modified_time = models.DateTimeField()    #文章最后修改时间。
    excerpt = models.CharField(max_length=200, blank=True)    #文章摘要，允许为空（blank=True）。
    
    #分类调用，一对多，一篇文章对应一个分类。
    category = models.ForeignKey(Category)
    #标签调用，多对一（一篇文章下有多个标签，ManyToManyField）。
    tags = models.ManyToManyField(Tag, blank=True)

    #文章作者，User是从django.contrib.auth.models（django内置应用）导入的
    #User是django先前写好的用户模型。
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    #自定义 get_absolute_url 方法
    def get_absolute_url(self):
        return reverse('blogapp:detail', kwargs={'pk': self.pk})