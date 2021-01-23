from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, CategoryView, AddCategoryView, SettingView, ProfileView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="detail"),
    path('post/', AddPostView.as_view(), name='post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update'),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name='delete'),
    path('article/category/<int:cats>', CategoryView, name='classify'),
    path('add_category/', AddCategoryView.as_view(), name="category"),
    path('setting/', SettingView.as_view(), name="setting"),
    path('profile/', ProfileView, name="profile"),
]
