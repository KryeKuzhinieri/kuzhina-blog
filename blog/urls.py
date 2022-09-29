from django.urls import path
from .views import homepage, post, about, category_post_list, all_posts, search


urlpatterns = [
    path('', homepage, name="homepage"),
    path('post/<slug>', post, name="post"),
    path('about/', about, name="about"),
    path('category_post_list/<slug>', category_post_list, name="category_post_list"),
    path('all_posts/', all_posts, name="all_posts"),
    path('search/', search, name="search"),
]
