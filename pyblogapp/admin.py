from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
# Register your models here.
from .models import Post
class PostmodelAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","author","pub_date"]
admin.site.register(Post,PostmodelAdmin)
