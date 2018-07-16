from django.db import models
from django.contrib.auth.models import User
from slugify import slugify
from .fields import OrderField


class Course(models.Model):
    user = models.ForeignKey(User, related_name='courses_user', on_delete=models.CASCADE, verbose_name='用户')
    title = models.CharField(max_length=200, verbose_name='标题')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='SLUG')
    overview = models.TextField(verbose_name='概览')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 多对多不需要on_delete参数
    student = models.ManyToManyField(User, related_name="courses_joined", blank=True, verbose_name='学生')

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name
        ordering = ('-created',)

    def save(self, *args, **kargs):
        self.slug = slugify(self.title)
        super(Course, self).save(*args, **kargs)

    def __str__(self):
        return self.title


# instance是Lesson的实例，filename是文件名
def user_directory_path(instance, filename):
    return "courses/user_{0}/{1}".format(instance.user.id, filename)


class Lesson(models.Model):
    user = models.ForeignKey(User, related_name='lesson_user', on_delete=models.CASCADE, verbose_name='用户')
    course = models.ForeignKey(Course, related_name='lesson', on_delete=models.CASCADE, verbose_name='课程')
    title = models.CharField(max_length=200, verbose_name='章节')
    video = models.FileField(upload_to=user_directory_path, verbose_name='视频地址')
    description = models.TextField(blank=True, verbose_name='章节描述')
    attach = models.FileField(blank=True, upload_to=user_directory_path, verbose_name='附件地址')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    order = OrderField(blank=True, for_fields=['course'])

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name
        ordering = ['order']

    def __str__(self):
        return '{}.{}'.format(self.order, self.title)

