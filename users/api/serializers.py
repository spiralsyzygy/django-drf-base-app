from django.contrib.auth import password_validation as validators
from django.contrib.auth.models import Group
from django.core import exceptions
from rest_framework import serializers
from users.models import User



class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def validate(self, data):
         # here data has all the fields which have validated values
         # so we can create a User instance out of it
         user = User(**data)

         # get the password from the data
         password = data.get('password')

         errors = dict()
         try:
             # validate the password and catch the exception
             validators.validate_password(password=password, user=User)

         # the exception raised here is different than serializers.ValidationError
         except exceptions.ValidationError as e:
             errors['password'] = list(e.messages)

         if errors:
             raise serializers.ValidationError(errors)

         return super(SignUpSerializer, self).validate(data)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class PasswordChangeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('password')
