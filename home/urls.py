from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView,UpdatePostView, DeletePostView,AddCategoryView, CategoryView

urlpatterns = [
    path('category/<str:cats>/', CategoryView, name='category'),
    path('add_category/', AddCategoryView.as_view(), name='add-category' ),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete-post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('add_post/', AddPostView.as_view(), name='add-post' ),
    path('article/<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
    path('',HomeView.as_view(), name='home'),
]
