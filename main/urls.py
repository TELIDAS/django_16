from django.contrib import admin
from django.urls import path
from blog.views import hello_world, all_posts


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('posts/', all_posts),
]
