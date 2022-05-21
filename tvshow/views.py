from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from . import models, forms
from datetime import datetime, timedelta

start_date = datetime.today() - timedelta(days=5)


def tv_show(request):
    queryset = models.Shows.objects.order_by("-id")
    return render(request, "shows_all.html", {"shows": queryset})


def tv_show_latest(request):
    queryset = models.Shows.objects.filter(created_date__gt=start_date).order_by("-id")
    return render(request, "shows_all.html", {"shows": queryset})


def tv_show_drama(request):
    queryset = models.Shows.objects.filter(genre="Drama").order_by("-id")
    return render(request, "shows_all.html", {"shows": queryset})


def tv_show_horror(request):
    queryset = models.Shows.objects.filter(genre="Horror").order_by("-id")
    return render(request, "shows_all.html", {"shows": queryset})


def tv_show_comedy(request):
    queryset = models.Shows.objects.filter(genre="Comedy").order_by("-id")
    return render(request, "shows_all.html", {"shows": queryset})


def tv_show_fantasy(request):
    queryset = models.Shows.objects.filter(genre="Fantasy").order_by("-id")
    return render(request, "shows_all.html", {"shows": queryset})


def tv_show_sci_fi(request):
    queryset = models.Shows.objects.filter(genre="Sci-Fi").order_by("-id")
    return render(request, "shows_all.html", {"shows": queryset})


def tv_show_onime(request):
    queryset = models.Shows.objects.filter(genre="Anime").order_by("-id")
    return render(request, "shows_all.html", {"shows": queryset})


def tv_show_romantic(request):
    queryset = models.Shows.objects.filter(genre="Romantic").order_by("-id")
    return render(request, "shows_all.html", {"shows": queryset})


def tv_show_action(request):
    queryset = models.Shows.objects.filter(genre="Action").order_by("-id")
    return render(request, "shows_all.html", {"shows": queryset})


def get_show_detail(request, id):
    object = get_object_or_404(models.Shows, id=id)
    return render(request, "shows_detail.html", {"show": object})


def add_show(request):
    method = request.method
    if method == "POST":
        form = forms.TVShowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return HttpResponse("TVShow Created successfully")
            return redirect(reverse("shows_url:shows_all_url"))
    else:
        form = forms.TVShowForm()
    return render(request, "add_shows.html", {"form": form})


def show_update(request, id):
    show_object = get_object_or_404(models.Shows, id=id)
    if request.method == "POST":
        form = forms.TVShowForm(instance=show_object, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("shows_url:shows_all_url"))
    else:
        form = forms.TVShowForm(instance=show_object)
    return render(request, "show_update.html", {"form": form,
                                                "object": show_object})


def show_delete(request, id):
    show_object = get_object_or_404(models.Shows, id=id)
    show_object.delete()
    return redirect(reverse("shows_url:shows_all_url"))
