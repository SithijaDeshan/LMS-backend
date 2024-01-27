from rest_framework import serializers
from .models import User
from .models import Books
from rest_framework.authtoken.views import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

        extra_kwargs = {'password': {
            'write_only': True,
            'required': True
        }}

    def create(self, validated_data):
        user= User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'