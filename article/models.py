from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from slugify import slugify


class ArticleColumn(models.Model):
    user = models.ForeignKey(User, related_name='article_column', on_delete=models.CASCADE, verbose_name='作者')
    column = models.CharField(max_length=200, verbose_name='栏目名')
    created = models.DateField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '栏目'
        verbose_name_plural = verbose_name
        ordering = ("-created",)

    def __str__(self):
        return self.column


class ArticleTag(models.Model):
    author = models.ForeignKey(User, related_name="tag", on_delete=models.CASCADE, verbose_name='作者')
    tag = models.CharField(max_length=500, verbose_name='标签')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag


class ArticlePost(models.Model):
    author = models.ForeignKey(User, related_name="article", on_delete=models.CASCADE, verbose_name='作者')
    title = models.CharField(max_length=200, verbose_name='作者')
    slug = models.SlugField(max_length=500, verbose_name='SLUG')
    column = models.ForeignKey(ArticleColumn, related_name="article_column", on_delete=models.CASCADE, verbose_name='栏目')
    body = models.TextField(verbose_name='正文')
    created = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    users_like = models.ManyToManyField(User, related_name="articles_like", blank=True, verbose_name='喜欢的人')
    article_tag = models.ManyToManyField(ArticleTag, related_name='article_tag', blank=True, verbose_name='标签')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        # ordering = ("title",)
        ordering = ("-updated",)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    # 如果没有填写slug，则使用slugify从标题读取
    def save(self, *args, **kargs):
        self.slug = slugify(self.title)
        super(ArticlePost, self).save(*args, **kargs)

    # URL绝对地址
    def get_absolute_url(self):
        return reverse("article:article_detail", args=[self.id, self.slug])

    def get_url_path(self):
        return reverse("article:list_article_detail", args=[self.id, self.slug])


class Comment(models.Model):
    article = models.ForeignKey(ArticlePost, related_name="comments", on_delete=models.CASCADE, verbose_name='文章')
    commentator = models.CharField(max_length=90, verbose_name='评论者')
    body = models.TextField(verbose_name='评论')
    created = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ('-created',)

    def __str__(self):
        return "{0} 对 {1} 的评论".format(self.commentator, self.article)

