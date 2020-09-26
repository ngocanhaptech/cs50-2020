from django.db import models
from django.utils import timezone
# from django.utils.text import  slugify
from blogsite.utils import unique_slugify
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES =  (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish', blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    body = RichTextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    def save(self, *args, **kwargs):
        unique_slugify(self, self.title, slug_field_name='slug', queryset=None, slug_separator='-')
        super(Post, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ('-publish',)
    
    def get_absolute_url(self):
        return reverse('blog:post_detail',
            [self.slug])
    
    def __str__(self):
        return self.title
