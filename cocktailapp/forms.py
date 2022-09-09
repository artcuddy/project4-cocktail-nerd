from .models import Comment, Post, Profile
from django.contrib.auth.models import User
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


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={
                                'class':
                                'form-control'
                                }))
    email = forms.EmailField(required=False,
                             widget=forms.TextInput(attrs={
                                'class':
                                'form-control'
                                }))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 5
        }))

    class Meta:
        model = Profile
        fields = ['bio']
