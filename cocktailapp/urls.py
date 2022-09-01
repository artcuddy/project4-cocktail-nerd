from django.urls import path

from . import views
from .views import account_login_view, account_signup_view
from .views import account_logout_view, SearchResultsView
from .views import UpdatePostView, DeletePostView


urlpatterns = [

    path('account/login/', view=account_login_view, name='login'),
    path('account/signup/', view=account_signup_view, name='signup'),
    path('account/logout/', view=account_logout_view, name='logout'),
    path("search_posts/", SearchResultsView.as_view(), name="search_posts"),
    path('category/<category>/', views.CatListView.as_view(), name='category'),
    path('all_cocktails/', views.PostList.as_view(), name='all_cocktails'),
    path('', views.FeaturedList.as_view(), name='home'),
    path('add_post/', views.add_cocktail, name='add_post'),
    path(
        'article/edit/<slug:slug>/',
        UpdatePostView.as_view(),
        name='edit_post'
        ),
    path(
        'article/<slug:slug>/delete',
        DeletePostView.as_view(),
        name='delete_post'
        ),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]

handler404 = "cocktailapp.views.page_not_found_view"
