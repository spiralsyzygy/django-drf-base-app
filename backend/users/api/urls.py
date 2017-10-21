from django.conf.urls import include, url
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from .views import UserViewSet, GroupViewSet, SignUpView, PasswordChangeView
from django.views.decorators.csrf import csrf_exempt

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^signup/', SignUpView.as_view(), name='api-signup'),
    url(r'^token-auth/', obtain_jwt_token, name='token-auth'),
    url(r'^password_change/(?P<pk>\d+)/$', PasswordChangeView.as_view(), name='api-password-change')
]
