from django.urls import path
from . import views


app_name = "shows_url"
urlpatterns = [
    path('shows/', views.tv_show, name="shows_all_url"),
    path('shows/latest/', views.tv_show_latest, name="latest"),
    path('shows/drama/', views.tv_show_drama, name="drama"),
    path('shows/horror/', views.tv_show_horror, name="horror"),
    path('shows/comedy/', views.tv_show_comedy, name="comedy"),
    path('shows/fantasy/', views.tv_show_fantasy, name="fantasy"),
    path('shows/scifi/', views.tv_show_sci_fi, name="scifi"),
    path('shows/onime/', views.tv_show_onime, name="onime"),
    path('shows/romantic/', views.tv_show_romantic, name="romantic"),
    path('shows/action/', views.tv_show_action, name="action"),
    path('shows/<int:id>/', views.get_show_detail, name="show"),
    path('shows/<int:id>/update/', views.show_update, name="show_update"),
    path('shows/<int:id>/delete/', views.show_delete, name="show_delete"),
    path('add-shows/', views.add_show, name="add_show"),
]
