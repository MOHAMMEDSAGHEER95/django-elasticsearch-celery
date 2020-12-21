from django.contrib import admin

# Register your models here.
from applications.blogs.models import Blog
from applications.blogs.tasks import save_user_details


class BlogAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        save_user_details.delay(request.user.id, obj.id)


admin.site.register(Blog, BlogAdmin)
