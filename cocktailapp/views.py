from django.shortcuts import(
    render, get_object_or_404, reverse)
from django.views import generic, View
from django.http import HttpResponseRedirect
from allauth.account.views import LoginView, SignupView 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CommentForm
from .models import *

from allauth.account.views import SignupView, LogoutView, LoginView


class AccountSignupView(SignupView):
    # Signup View extended
    # change template's name and path
    template_name = "account/signup.html"

account_signup_view = AccountSignupView.as_view()


class AccountLoginView(LoginView):
    # Login View extended
    # change template's name and path
    template_name = "account/login.html"

account_login_view = AccountLoginView.as_view()


class AccountLogoutView(LogoutView):
    # Logout View extended
    # change template's name and path
    template_name = "account/logout.html"

account_logout_view = AccountLogoutView.as_view()


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "home.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )

def categories(request):
    """
    Renders the categories page
    """
    return render(request, 'categories.html')


def categories_view(request, cats):
    """
    Renders the posts filtered by categories
    """
    categories_posts = Post.objects.filter(
        categories__title__contains=cats, status=1)
    return render(request, 'categories_posts.html', {
        'cats': cats.title(), 'categories_posts': categories_posts})


class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

