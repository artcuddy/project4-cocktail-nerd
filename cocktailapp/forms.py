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
            'status',
            'title',
            'categories',
            'featured_image',
            'content',
            'ingredients',
            'steps'
            )

        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'categories': forms.Select(attrs={'class': 'form-control'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'content': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
            'steps': SummernoteWidget(),
        }
