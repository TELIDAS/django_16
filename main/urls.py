from django.contrib import admin
from django.urls import path, include
from blog.views import hello_world, all_posts
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = (
        [
            path('admin/', admin.site.urls),
            path('', include('tvshow.urls')),
            path('', include('blog.urls')),
            path('', include('scrapy.urls')),
        ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
