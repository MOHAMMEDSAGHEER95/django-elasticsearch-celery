from django.contrib import admin

# Register your models here.
from applications.blogs.models import Blog

admin.site.register(Blog)
