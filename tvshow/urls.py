from django.urls import path
from . import views


app_name = "shows_url"
urlpatterns = [
    path('shows/', views.tv_show, name="shows_all_url"),
    path('shows/<int:id>/', views.get_show_detail, name="show"),
    path('add-shows/', views.add_show, name="add_show"),
]
