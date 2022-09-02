from django.shortcuts import (
     render, get_object_or_404, reverse)
from django.views import generic, View
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import CommentForm, CocktailForm
from .models import Post, Category
from allauth.account.views import LoginView, SignupView, LogoutView
from django.urls import reverse_lazy


# Signup view
class AccountSignupView(SignupView):
    # Signup View extended
    # change template's name and path
    template_name = "account/signup.html"


account_signup_view = AccountSignupView.as_view()


# Login view
class AccountLoginView(LoginView):
    # Login View extended
    template_name = "account/login.html"


account_login_view = AccountLoginView.as_view()


# Logout view
class AccountLogoutView(LogoutView):
    # Logout View extended
    template_name = "account/logout.html"


account_logout_view = AccountLogoutView.as_view()


# Post list view
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(
        status=1).order_by("-created_on").exclude(categories=6)
    template_name = "all_cocktails.html"
    paginate_by = 6


# Single post detail view
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


# Update post
class UpdatePostView(UpdateView):
    model = Post
    form_class = CocktailForm
    template_name = 'edit_post.html'


# Delete post
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy("all_cocktails")


# Manage all posts list view
class ManageAllPostsList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(
        status=1).order_by("-created_on").filter(featured=1)
    template_name = "manage_posts.html"
    paginate_by = 6


# Featured posts list view
class FeaturedList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(
        status=1).order_by("-created_on").filter(featured=1)
    template_name = "home.html"
    paginate_by = 6


# Related list view
def related_list(request):
    related_list = Post.objects.filter(
        status=1).order_by("-created_on").filter(featured=1)
    context = {
        'related_list': related_list,
    }
    return context


# Homepage view
def home(request):
    """
    Renders the home page
    """
    return render(request, 'home.html')


# Post like view
class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# Category list view
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


# Category list
def category_list(request):
    category_list = Category.objects.exclude(title='default')
    context = {
        'category_list': category_list,
    }
    return context


# All categories list view
class AllCategoriesList(generic.ListView):
    model = Category
    template_name = "all_categories.html"
    paginate_by = 12

    def get_queryset(self):
        category_list = Category.objects.exclude(title='default')
        return category_list


# Add category view
class AddCategoryView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'add_category.html'


# Edit category view
class EditCategoryView(UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'edit_category.html'


# Delete Category
class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'delete_category.html'
    success_url = reverse_lazy("all_categories")


# Manage categories view
class ManageCategoriesView(ListView):
    model = Category
    fields = '__all__'
    template_name = 'manage_categories.html'

    def get_queryset(self):
        category_list = Category.objects.exclude(title='default')
        return category_list


# Search results view
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


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
