from django.contrib.auth.models import Group
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, UpdateAPIView
from .serializers import (UserSerializer, GroupSerializer,
                          SignUpSerializer, PasswordChangeSerializer)
from django.contrib.auth import get_user_model

User = get_user_model()


class SignUpView(CreateAPIView):
    """
    API endpoint that allows users to signup.
    """
    # model = User
    # queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]
    serializer_class = SignUpSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PasswordChangeView(UpdateAPIView):
    """
    API endpoint that allows authenticated users to change their password
    """
    serializer_class = PasswordChangeSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    queryset = User.objects.all()

    def patch(self, request, pk, format=None):
        user = User.objects.get(pk=pk)
        if user == request.user:
            user.set_password(request.data['password'])
            user.save()
            return Response(status=204)
        return Response(status=400)
