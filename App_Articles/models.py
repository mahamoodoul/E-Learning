from django.db import models
from App_Login.models import User, user_type
# Create your models here.



class Category(models.Model):
    category = models.CharField(max_length=264, verbose_name="Mention your Category Articles")
    def __str__(self):
        return str(self.category)
class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles_author')
    articles_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='video_cat')
    articles_title = models.CharField(max_length=264, verbose_name="Put a Title")
    slug = models.SlugField(max_length=264, unique=True)
    articles_content = models.TextField(verbose_name="What is on your mind?")
    articles_image = models.ImageField(upload_to='blog_images', verbose_name="Image")
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date',]

    def __str__(self):
        return self.articles_title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-comment_date',)

    def __str__(self):
        return self.comment
