from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _


class Blog(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()

    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')

    def __str__(self):
        return self.title
