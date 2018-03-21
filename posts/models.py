from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    subtitle = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='static/img/photo', height_field=None, width_field=None ,default='static/img/default.jpg')
    likes = models.PositiveSmallIntegerField(default=0)
    dislikes = models.PositiveSmallIntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=50)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    assos_post = models.ManyToManyField('Post')

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey('auth.User')
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    on_post = models.ForeignKey('Post')

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.author.username