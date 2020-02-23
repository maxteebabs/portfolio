from django.db import models
from . import views
import uuid

# Create your models here.
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=50, db_index=True, editable=False)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    summary = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
         if not self.slug:
            self.slug = str(uuid.uuid1())
         super().save(*args, **kwargs)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('show_project', args=[str(self.slug)])

