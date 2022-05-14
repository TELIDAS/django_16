from django.urls import path
from . import views

urlpatterns = [
    path('shows/', views.tv_show, name="shows_all_url"),
    path('shows/<int:id>/', views.get_show_detail, name="show_url"),
]
