from rest_framework import viewsets

from .serializers import PostSerializer
from .serializers import SlideShowSerializer
from .serializers import StaffSerializer

from posts.models import Post
from slideshow.models import SlideShow
from staff.models import Staff


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class SlideShowViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SlideShow.objects.all()
    serializer_class = SlideShowSerializer

class StaffViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
