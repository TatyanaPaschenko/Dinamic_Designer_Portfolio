from django.contrib import admin
from .models import PhotoModel, Feedback
from design.forms import ContactForm
from django.db import models
from django.forms import widgets


class PhotoModelAdmin(admin.ModelAdmin):
    model = PhotoModel
    fields = ['name', 'short_description',
              'description', 'mini_image_title',
              'first_image_comp', 'first_or_lending_image',
              'second_image']


class FeedbackAdmin(admin.ModelAdmin):
    model = Feedback
    list_display = ["from_email", "create_date"]


admin.site.register(PhotoModel, PhotoModelAdmin)
admin.site.register(Feedback)


