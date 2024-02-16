from rest_framework import serializers
from . import views
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model=User
        fields=['id', 'username', 'password', 'email']