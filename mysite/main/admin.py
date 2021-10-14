from django.contrib import admin
from .models import tutorial
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.
class TutorialAdmin(admin.ModelAdmin):
    

    formfield_overrides={

        models.TextField:{"widget":TinyMCE()}
    }
admin.site.register(tutorial,TutorialAdmin)