from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db import models

User = get_user_model()


def user_directory_path(instance, filename):
    return f'posts{instance}/{filename}'


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class BlogManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_author')
    title = models.CharField(max_length=200)
    excerpt = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blog_category')
    slug = models.SlugField(max_length=250, unique_for_date='publish_date')
    publish_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=BlogManager.options, default='draft')
    image = models.ImageField(upload_to=user_directory_path, default='posts/default.png')

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    blog_manager = BlogManager()

    class Meta:
        ordering = ('-publish_date',)

    def __str__(self):
        return self.title
