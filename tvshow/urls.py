from django.urls import path
from . import views, models
from datetime import datetime, timedelta

start_date = datetime.today() - timedelta(days=5)

app_name = "shows_url"
urlpatterns = [
    path('shows/', views.TVShowListView.as_view(), name="shows_all_url"),
    path('shows/latest/', views.TVShowListView.as_view(
        queryset=models.Shows.objects.filter(
            created_date__gt=start_date
        ).order_by("-id")
    ), name="latest"),
    path('shows/drama/', views.TVShowListView.as_view(
        queryset=models.Shows.objects.filter(genre="Drama").order_by("-id"),
    ), name="drama"),
    path('shows/horror/', views.TVShowListView.as_view(
        queryset=models.Shows.objects.filter(genre="Horror").order_by("-id"),
    ), name="horror"),
    path('shows/comedy/', views.TVShowListView.as_view(
        queryset=models.Shows.objects.filter(genre="Comedy").order_by("-id"),
    ), name="comedy"),
    path('shows/fantasy/', views.TVShowListView.as_view(
        queryset=models.Shows.objects.filter(genre="Fantasy").order_by("-id"),
    ), name="fantasy"),
    path('shows/scifi/', views.TVShowListView.as_view(
        queryset=models.Shows.objects.filter(genre="Sci-Fi").order_by("-id"),
    ), name="scifi"),
    path('shows/onime/', views.TVShowListView.as_view(
        queryset=models.Shows.objects.filter(genre="Anime").order_by("-id"),
    ), name="onime"),
    path('shows/romantic/', views.TVShowListView.as_view(
        queryset=models.Shows.objects.filter(genre="Romantic").order_by("-id"),
    ), name="romantic"),
    path('shows/action/', views.TVShowListView.as_view(
        queryset=models.Shows.objects.filter(genre="Action").order_by("-id"),
    ), name="action"),
    path('shows/<int:id>/', views.TVShowDetailView.as_view(), name="show"),
    path('shows/<int:id>/update/', views.TVShowUpdateView.as_view(), name="show_update"),
    path('shows/<int:id>/delete/', views.TVShowsDeleteView.as_view(), name="show_delete"),
    path('add-shows/', views.TVShowCreateView.as_view(), name="add_show"),
]
