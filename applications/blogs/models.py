from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _


class Blog(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')

    def __str__(self):
        return self.title
