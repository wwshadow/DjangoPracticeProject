from django.db import models
from django.contrib.auth.models import User
from slugify import slugify


class Image(models.Model):
    user = models.ForeignKey(User, related_name="images", on_delete=models.CASCADE, verbose_name='用户')
    title = models.CharField(max_length=300, verbose_name='标题')
    url = models.URLField(verbose_name='网址')
    slug = models.SlugField(max_length=500, blank=True, verbose_name='SLUG')
    description = models.TextField(blank=True, verbose_name='描述')
    created = models.DateField(auto_now_add=True, db_index=True, verbose_name='创建时间')
    image = models.ImageField(upload_to='images/%Y/%m/%d', verbose_name='图片地址')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '图片'
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)

