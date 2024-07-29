from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Pendidikan(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    postname = models.CharField(max_length=600)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pendidikan = models.ForeignKey(Pendidikan, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/posts', blank=True, null=True)
    content = RichTextField()
    link = models.URLField(max_length=200, blank=True, null=True)  # Field baru untuk link
    created = models.DateTimeField(default=timezone.now)  # Field baru untuk created
    updated = models.DateTimeField(auto_now=True) 
    time = models.CharField(default=timezone.now().strftime("%d %B %Y"), max_length=100, blank=True)
    
    def __str__(self):
        return str(self.postname)

class Contact(models.Model):
    name = models.CharField(max_length=600)
    email = models.EmailField(max_length=600)
    subject = models.CharField(max_length=1000)
    message = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
