from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from . import models, forms


def tv_show(request):
    queryset = models.Shows.objects.all()
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
