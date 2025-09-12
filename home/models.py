# ciu/models.py
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="news/")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to="events/")

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()
    photo = models.ImageField(upload_to="testimonials/", blank=True, null=True)
