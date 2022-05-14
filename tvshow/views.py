from django.shortcuts import render, get_object_or_404
from . import models


def tv_show(request):
    queryset = models.Shows.objects.all()
    return render(request, "shows_all.html", {"shows": queryset})


def get_show_detail(request, id):
    object = get_object_or_404(models.Shows, id=id)
    return render(request, "shows_detail.html", {"show": object})
