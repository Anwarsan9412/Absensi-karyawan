from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from phone_field import PhoneField
from django.utils import timezone
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField( null=True ,blank=True, upload_to="profile_pics", default='profil.png')
    jenis_kelamin = models.CharField( max_length=50)
    status_nikah = models.CharField(default='belum', max_length=50)
    alamat        = models.CharField(max_length=255)
    divisi        = models.CharField(max_length=100)
    jabatan       = models.CharField(max_length=100)
    phone         = PhoneField(blank=True, help_text='Contact phone number')
    
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):
        super().save()
        
        img = Image.open(self.profile_pic.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
    


class Post(models.Model):
    title  = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # body   = models.TextField()
    body = RichTextField(blank=True, null=True)
    category = models.CharField(max_length=255, default='berita')
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, default='berita')
    updated       = models.DateField(auto_now=True)
    published     = models.DateTimeField(auto_now_add=True)
    slug          = models.SlugField(unique=True,editable=False)
    
    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()
        
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        # return reverse('article-detail', args= (str(self.id)))
        return reverse('home')
    
    
    
    