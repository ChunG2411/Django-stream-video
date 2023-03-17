from django.contrib import admin
from .models import Video

# Register your models here.
class VideoAdmin(admin.ModelAdmin):
    model = Video
    list_display = ('name',)

admin.site.register(Video, VideoAdmin)