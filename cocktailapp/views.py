from django.shortcuts import (
     render, get_object_or_404, reverse, redirect)
from django.views import generic, View
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import CommentForm, CocktailForm, UpdateUserForm, UpdateProfileForm
from .models import Post, Category, Comment, Profile
from allauth.account.views import LoginView, SignupView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import template

register = template.Library()


# Signup view
class AccountSignupView(SignupView):
    """
    Sign-up view extended
    """
    template_name = "account/signup.html"


account_signup_view = AccountSignupView.as_view()


# Login view
class AccountLoginView(LoginView):
    """
    Login view extended
    """
    template_name = "account/login.html"


account_login_view = AccountLoginView.as_view()


# Logout view
class AccountLogoutView(LogoutView):
    """
    Logout view extended
    """
    template_name = "account/logout.html"


account_logout_view = AccountLogoutView.as_view()


# Post list view
class PostList(generic.ListView):
    """
    Post List view show all cocktails
    """
    model = Post
    queryset = Post.objects.filter(
        status=1).order_by("-created_on").exclude(categories=7)
    template_name = "all_cocktails.html"
    paginate_by = 9


# Single post detail view
class PostDetail(View):
    """
    Single post detail view gets posts details
    """
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
        """
        Single post detail view POSTS posts details
        """
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
class UpdatePostView(SuccessMessageMixin, UpdateView):
    """
    Update post detail view edit and update the post
    """
    model = Post
    form_class = CocktailForm
    template_name = 'edit_post.html'
    success_message = 'The cocktail was edited successfully!'
    success_url = reverse_lazy("manage_posts")


# Delete post
class DeletePostView(DeleteView):
    """
    Delete post detail view delete the post
    """
    model = Post
    template_name = 'delete_post.html'
    success_message = 'The cocktail was successfully deleted!'
    success_url = reverse_lazy("manage_posts")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeletePostView, self).delete(request, *args, **kwargs)


# Manage all posts list view
class ManageAllPostsList(LoginRequiredMixin, generic.ListView):
    """
    Manage all posts shows post managment page
    to edit or delete the posts
    """
    model = Post
    queryset = Post.objects.filter(
        status=1).order_by("-created_on")
    template_name = "manage_posts.html"
    paginate_by = 12


# Featured posts list view
class FeaturedList(generic.ListView):
    """
    Featured post list view shows the featured
    cocktails on the homepage
    """
    model = Post
    queryset = Post.objects.filter(
        status=1).order_by("-created_on").filter(featured=1)
    template_name = "home.html"
    paginate_by = 6


# Related list view shows the sidebar featured posts
def related_list(request):
    """
    Related list view shows the sidebar featured posts
    """
    related_list = Post.objects.filter(
        status=1).order_by('-created_on').filter(featured=1)[:6]
    context = {
        'related_list': related_list,
    }
    return context


# Homepage view renders the homepage
def home(request):
    """
    Renders the home page
    """
    return render(request, "home.html")


# Post like view
class PostLike(LoginRequiredMixin, View):
    """
    Post like view enables the post to be liked
    by the user
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.success(
                request,
                'What a shame you unliked this cocktail!'
                )
        else:
            post.likes.add(request.user)
            messages.success(
                request,
                'Thanks you liked this cocktail!'
                )
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# Liked posts list view shows the users liked cocktails page
@login_required
def liked_list(request):
    """
    Liked posts list view shows
    the users liked cocktails page
    """
    liked_list = Post.objects.filter(likes=request.user)
    total_liked_list = liked_list.count()
    context = {
        'liked_list': liked_list,
        'total_liked_list': total_liked_list,
    }
    return render(request, "liked_posts.html", context)


# Total user liked posts view shows the users total liked cocktails count
def total_liked_list(request):
    """
    Total user liked posts view shows the
    users total liked cocktails count
    """
    if request.user.is_anonymous:
        total_liked_list = False
        context = {
            'total_liked_list': total_liked_list,
        }
        return context
    else:
        liked_list = Post.objects.filter(likes=request.user)
        total_liked_list = liked_list.count()
        context = {
            'total_liked_list': total_liked_list,
        }
        return context


# Category list view
class CatListView(ListView):
    """
    Cat List view shows the list of categories
    """
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
    """
    Categories list displays the all categories
    page
    """
    category_list = Category.objects.exclude(title='default')
    context = {
        'category_list': category_list,
    }
    return context


# All categories list view
class AllCategoriesList(generic.ListView):
    """
    All categories list displays the all categories
    page
    """
    model = Category
    template_name = "all_categories.html"
    paginate_by = 6

    def get_queryset(self):
        category_list = Category.objects.exclude(title='default')
        return category_list


# Add category view
class AddCategoryView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Add category view displays the add category
    page
    """
    model = Category
    fields = '__all__'
    template_name = 'add_category.html'
    success_message = 'The category was added successfully!'
    success_url = reverse_lazy("manage_categories")


# Edit category view
class EditCategoryView(SuccessMessageMixin, UpdateView):
    """
    Edit category view displays the edit category
    page
    """
    model = Category
    fields = '__all__'
    template_name = 'edit_category.html'
    success_message = 'The category was edited successfully!'
    success_url = reverse_lazy("manage_categories")


# Delete Category
class DeleteCategoryView(DeleteView):
    """
    Delete category view displays the delete category
    page
    """
    model = Category
    template_name = 'delete_category.html'
    success_url = reverse_lazy("manage_categories")
    success_message = 'The category was successfully deleted!'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteCategoryView, self).delete(request, *args, **kwargs)


# Manage categories view
class ManageCategoriesView(LoginRequiredMixin, ListView):
    """
    Manage categories view displays the manage categories
    page to enabel the user to edit or delete categories
    """
    model = Category
    fields = '__all__'
    paginate_by = 8
    template_name = 'manage_categories.html'

    def get_queryset(self):
        category_list = Category.objects.exclude(title='default')
        return category_list


# Search results view
class SearchResultsView(ListView):
    """
    Search results view displays the search results
    page
    """
    model = Post
    template_name = 'search_posts.html'

    def get_queryset(self):
        query = self.request.GET.get("searched", default="")
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(ingredients__icontains=query)
        )
        return object_list


# Create new cocktail post
@login_required
def add_cocktail(request):
    """
    Create new cocktail post
    """
    submitted = False
    if request.method == 'POST':
        # handle the POST request here
        form = CocktailForm(request.POST, request.FILES)
        if all([form.is_valid()]):
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            messages.success(
                request,
                'Your cocktail was submitted successfully!'
                )
            return HttpResponseRedirect('/add_post?submitted=True')
    else:
        form = CocktailForm
        if 'submitted' in request.GET:
            submitted = True

    return render(
        request, 'add_post.html', {'form': form, 'submitted': submitted})


# Delete users comment
@login_required
def delete_comment(request, comment_id):
    """
    Delete users comment
    """
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    messages.success(request, 'The comment was deleted successfully!')
    return HttpResponseRedirect(reverse(
        'post_detail', args=[comment.post.slug]))


# Edit users comment
class EditComment(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Edit users comment
    """
    model = Comment
    template_name = 'edit_comment.html'
    form_class = CommentForm
    success_message = 'The comment was successfully updated!'


# Edit user profile
@login_required
def profile(request):
    """
    Edit user profile
    """
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(
            request.POST, request.FILES,
            instance=request.user.profile
            )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has updated successfully!')
            return redirect(to='profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
        })


# Get all user profile data and make it available site wide
def show_all_users(request):
    """
    Get all user profile data and make it available site wide
    """
    data = Profile.objects.all()

    context = {
        'data': data
    }
    return context


# 404 Error page
def page_not_found_view(request, exception):
    """
    Display 404 Error page if requested page not found
    """
    return render(request, '404.html', status=404)
