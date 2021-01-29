from .models import Post, Category
from rest_framework import serializers 
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = User  
        fields = ['username', 'first_name', 'last_name']


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False)
    category = CategorySerializer(required=False)

    class Meta:  
        model = Post  
        fields = '__all__'
