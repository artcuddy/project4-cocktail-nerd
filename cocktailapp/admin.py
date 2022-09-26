from django.contrib import admin
from .models import Post, Comment, Category, Profile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class postAdmin(SummernoteModelAdmin):
    """
    Add fields for Posts in admin panel
    """
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'categories', 'featured')
    list_display = (
        'title', 'categories', 'slug', 'author', 'status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content', 'ingredients', 'steps')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Add fields for Category in admin panel
    """
    list_display = ['title']
    search_fields = ['title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Add fields for Comments in admin panel
    """
    list_filter = ('approved', 'created_on')
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Profile)
