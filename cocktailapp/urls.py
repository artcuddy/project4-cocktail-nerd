from django.urls import path

from . import views
from .views import account_login_view, account_signup_view
from .views import account_logout_view, SearchResultsView
from .views import UpdatePostView, DeletePostView
from .views import AddCategoryView, AllCategoriesList
from .views import ManageCategoriesView, ManageAllPostsList
from .views import EditCategoryView, DeleteCategoryView
from django.conf.urls import include


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
        'manage_posts/',
        ManageAllPostsList.as_view(),
        name='manage_posts'
        ),
    path(
        'all_categories/',
        AllCategoriesList.as_view(),
        name='all_categories'
        ),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
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
    path(
        'manage_categories/',
        ManageCategoriesView.as_view(),
        name='manage_categories'
        ),
    path(
        'category/edit/<int:pk>',
        EditCategoryView.as_view(),
        name='edit_category'
        ),
    path(
        'category/<int:pk>/delete',
        DeleteCategoryView.as_view(),
        name='delete_category'
        ),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('delete_comment/<int:comment_id>', views.delete_comment,
         name='delete_comment'),
    path('edit_comment/<int:pk>', views.EditComment.as_view(),
         name='edit_comment'),
]

handler404 = "cocktailapp.views.page_not_found_view"
