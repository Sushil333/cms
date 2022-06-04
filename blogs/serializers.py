from rest_framework import serializers
from django.contrib.auth.models import User, Group

from blogs.models import Blog

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Blog
        fields = ['url', 'owner', 'title', 'content', 'created_at', 'updated_at', 'is_edited', 'verified']