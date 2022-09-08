from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify
from django.urls import reverse


STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    """
    Model for category
    """
    class Meta:
        verbose_name_plural = 'Categories'
    title = models.CharField(max_length=14, unique=True)
    category_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    """
    Model for posts
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    categories = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=7)
    featured_image = CloudinaryField("image", default="placeholder")
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    ingredients = models.TextField(blank=True)
    steps = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name="blogpost_like", blank=True)
    featured = models.BooleanField(default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Model for comments
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    def get_absolute_url(self):
        """Sets absolute URL"""
        return reverse('post_detail', args=[self.post.slug])
