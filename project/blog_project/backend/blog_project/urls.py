"""
URL configuration for blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog_app.views import get_posts, add_post, get_post_by_id

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', get_posts, name='get_posts'),           # Fetch all posts
    path('posts/add/', add_post, name='add_post'),         # Add a new post
    path('posts/<int:post_id>/', get_post_by_id, name='get_post_by_id'),  # Fetch post by ID
]
