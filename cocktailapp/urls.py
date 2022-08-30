from django.contrib import admin
from django.urls import path, include, re_path
from allauth.account.views import LoginView, SignupView, LogoutView

from . import views
from .views import account_login_view, account_signup_view, account_logout_view, SearchResultsView


urlpatterns = [

    path('account/login/', view=account_login_view, name='login'),
    path('account/signup/', view=account_signup_view, name='signup'),
    path('account/logout/', view=account_logout_view, name='logout'),
    path("search_posts/", SearchResultsView.as_view(), name="search_posts"),
    path('category/<category>/', views.CatListView.as_view(), name='category'),
    path('all_cocktails/', views.PostList.as_view(), name='all_cocktails'),
    path('all_bar_reviews/', views.BarList.as_view(), name='all_bar_reviews'),
    path('', views.FeaturedList.as_view(), name='home'),
    path('add_post/', views.blog_upload, name='add_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
