"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from users import views as users_views
from users.api import urls as users_api_urls


urlpatterns = [
    url(r'^api/', include(users_api_urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/', users_views.SignUpView.as_view(),name='signup'),
    url(r'^login/', users_views.LoginView.as_view(), name='login'),
    url(r'^password_change/', users_views.PasswordChange.as_view(), name='password_change'),
    url(r'^password_change/done/', users_views.PasswordChangeDone.as_view(), name='password_change_done'),
    # url(r'^password_reset/', users_views.PasswordChange.as_view(), name='password_reset'),
    url('^', include('django.contrib.auth.urls')),
]
