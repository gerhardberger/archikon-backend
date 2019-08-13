from rest_framework import serializers

from posts.models import Post
from slideshow.models import SlideShow
from staff.models import Staff

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'cover']

class SlideShowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SlideShow
        fields = ['id', 'image']

class StaffSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Staff
        fields = ['id', 'name', 'title_hu', 'title_en', 'email', 'phone', 'leader', 'image']
