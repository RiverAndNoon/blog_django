from django.db import models

# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    #作用是,当评论保存到数据库时,自动把时间值指定为当前时间
    created_time = models.DateTimeField(auto_now_add=True)

    #这个评论是关联某篇文章(Post)
    post = models.ForeignKey('blog.Post')
    def __str__(self):
        return self.text[20]