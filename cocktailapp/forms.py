from .models import Comment, Post
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CocktailForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = (
            'title',
            'status',
            'author',
            'categories',
            'featured_image',
            'content',
            'ingredients',
            'steps',
            'featured',
            )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'categories': forms.Select(attrs={'class': 'form-control'}),
            'content': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
            'steps': SummernoteWidget(),
        }
