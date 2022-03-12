"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from todo import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'todos', views.TodoView, 'todo')
router.register(r'job', views.RequestView, 'jobtype')
router.register(r'^article', views.ArticleView, 'article')
router.register(r'title', views.TitleView, 'title')
router.register(r'newjob', views.NewjobsView, 'newjob')
router.register(r'cjob', views.CjobsView, 'cjob')
router.register(r'ckra', views.CkraView, 'cjob')
router.register(r'newkra', views.NewkraView, 'cjob')
router.register(r'returns', views.ReturnsView, 'returns')

urlpatterns = [
path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^.*',TemplateView.as_view(template_name='index.html'))]



