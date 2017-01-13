from django.contrib import admin
from .models import PhotoModel


class PhotoModelAdmin(admin.ModelAdmin):
    model = PhotoModel
    fields = ['name', 'short_description',
              'description', 'mini_image_title',
              'first_image_comp', 'first_or_lending_image',
              'second_image']

admin.site.register(PhotoModel)
