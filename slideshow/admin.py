from django.contrib import admin
from adminsortable.admin import SortableAdmin

from .models import SlideShow

admin.site.register(SlideShow, SortableAdmin)
