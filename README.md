# DjangoPracticeProject

学习《跟老齐学Python:Django实战》的代码，附注释，基于Django2.0实现，实现的功能：
用户后台发布管理博客、文章、图片、课程，前台展示博客、文章、图片、课程

#### 使用方法 ####

```bash
git clone https://github.com/wenguonideshou/DjangoPracticeProject.git
cd DjangoPracticeProject
# 建表
python3 manage.py makemigrations
python3 manage.py migrate
# 创建管理员
python3 manage.py createsuperuser
# 运行网站
python3 manage.py runserver 0.0.0.0:80
```
