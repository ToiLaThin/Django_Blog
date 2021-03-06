from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField
import datetime

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=300)
    title_tag = models.CharField(max_length=300, default="Default title tag")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField()
    pub_date = models.DateField(default=timezone.now)
    category = models.CharField(max_length=300, default='nothing')
    snippet = models.CharField(
        max_length=300, default="Lorem ipsum dolor sit amet default text")
    # khoá ngoại tới bảng gồm bảng mquan hệ giữa Post và User
    likes = models.ManyToManyField(User, related_name='blogposts')

    header_image = models.ImageField(
        null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def likes_count(self):
        return self.likes.count()


class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_list')


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(
        null=True, blank=True, upload_to="images/profile/")
    blog_url = models.CharField(max_length=300, null=True, blank=True)
    fb_url = models.CharField(max_length=300, null=True, blank=True)
    zalo_url = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.user)
