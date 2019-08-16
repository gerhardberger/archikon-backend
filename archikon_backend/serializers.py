from rest_framework import serializers

from slideshow.models import SlideShow
from staff.models import Staff
from awards.models import Award
from about.models import About
from projects.models import Project, ProjectImageModel

class SlideShowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SlideShow
        fields = ['id', 'image']

class StaffSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Staff
        fields = ['id', 'name', 'title_hu', 'title_en', 'email', 'phone', 'leader', 'image', 'active']

class AwardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Award
        fields = ['id', 'name_hu', 'name_en', 'year', 'subtitle_hu', 'subtitle_en', 'link']

class AboutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = About
        fields = ['id', 'info_hu', 'info_en']

class ProjectImageModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectImageModel
        fields = ['image']

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    images = ProjectImageModelSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name_hu', 'name_en', 'location_hu', 'location_en', 'country_hu',
            'country_en', 'category', 'description_hu', 'description_en', 'thumbnail', 'images',
            'selected', 'listed']
