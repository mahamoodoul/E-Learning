from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

app_name = 'App_Articles'

urlpatterns = [
    path('create_articles',views.CreateArticles.as_view(), name='create_articles'),
     path(r'^?P<slug>[\w-]', views.articale_details, name='article_details'),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
