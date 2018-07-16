from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('blog/', include(("blog.urls", "blog"), namespace="blog")),
    path('account/', include(("account.urls", "account"), namespace='account')),
    path('pwd_reset/', include(("password_reset.urls", "pwd_reset"), namespace='pwd_reset')),
    path('article/', include(('article.urls', 'article'), namespace='article')),
    path('image/', include(('image.urls', 'image'), namespace='image')),
    path('course/', include(('course.urls', 'course'), namespace='course')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
