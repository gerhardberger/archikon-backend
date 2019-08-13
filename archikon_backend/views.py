from rest_framework import viewsets

from .serializers import SlideShowSerializer, StaffSerializer, AwardSerializer, AboutSerializer, ProjectSerializer

from slideshow.models import SlideShow
from staff.models import Staff
from awards.models import Award
from about.models import About
from projects.models import Project


class SlideShowViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SlideShow.objects.all()
    serializer_class = SlideShowSerializer

class StaffViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class AwardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer

class AboutViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
