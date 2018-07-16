from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.blog_title, name="blog_title"),
    path('<int:article_id>', views.blog_article, name="blog_article"),
]
