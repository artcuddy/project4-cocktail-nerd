from django.shortcuts import (
     render, get_object_or_404, reverse)
from django.views import generic, View
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import CommentForm, CocktailForm
from .models import Post, Category
from allauth.account.views import LoginView, SignupView, LogoutView


class AccountSignupView(SignupView):
    # Signup View extended
    # change template's name and path
    template_name = "account/signup.html"


account_signup_view = AccountSignupView.as_view()


class AccountLoginView(LoginView):
    # Login View extended
    template_name = "account/login.html"


account_login_view = AccountLoginView.as_view()


class AccountLogoutView(LogoutView):
    # Logout View extended
    template_name = "account/logout.html"


account_logout_view = AccountLogoutView.as_view()


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(
        status=1).order_by("-created_on").exclude(categories=6)
    template_name = "all_cocktails.html"
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


class FeaturedList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(
        status=1).order_by("-created_on").filter(featured=1)
    template_name = "home.html"
    paginate_by = 6


def related_list(request):
    related_list = Post.objects.filter(
        status=1).order_by("-created_on").filter(featured=1)
    context = {
        'related_list': related_list,
    }
    return context


def home(request):
    """
    Renders the home page
    """
    return render(request, 'home.html')


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class CatListView(ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(
                categories__title=self.kwargs['category']).filter(status=1)
        }
        return content


def category_list(request):
    category_list = Category.objects.exclude(
        title='default').exclude(title='bar review')
    context = {
        'category_list': category_list,
    }
    return context


class SearchResultsView(ListView):
    model = Post
    template_name = 'search_posts.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("searched", default="")
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(ingredients__icontains=query)
        )
        return object_list


# Create new post
@login_required
def add_cocktail(request):
    submitted = False
    if request.method == 'POST':
        # handle the POST request here
        form = CocktailForm(request.POST, request.FILES)
        if all([form.is_valid()]):
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return HttpResponseRedirect('/add_post?submitted=True')
    else:
        form = CocktailForm
        if 'submitted' in request.GET:
            submitted = True

    return render(
        request, 'add_post.html', {'form': form, 'submitted': submitted})
