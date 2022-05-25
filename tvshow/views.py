from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from . import models, forms
from datetime import datetime, timedelta
from django.views import generic

start_date = datetime.today() - timedelta(days=5)


class TVShowListView(generic.ListView):
    template_name = "shows_all.html"
    queryset = models.Shows.objects.order_by("-id")

    def get_queryset(self):
        return self.queryset


# def tv_show(request):
#     queryset = models.Shows.objects.order_by("-id")
#     return render(request, "shows_all.html", {"shows": queryset})
#
#
# def tv_show_latest(request):
#     queryset = models.Shows.objects.filter(created_date__gt=start_date).order_by("-id")
#     return render(request, "shows_all.html", {"shows": queryset})
#
#
# def tv_show_drama(request):
#     queryset = models.Shows.objects.filter(genre="Drama").order_by("-id")
#     return render(request, "shows_all.html", {"shows": queryset})
#
#
# def tv_show_horror(request):
#     queryset = models.Shows.objects.filter(genre="Horror").order_by("-id")
#     return render(request, "shows_all.html", {"shows": queryset})
#
#
# def tv_show_comedy(request):
#     queryset = models.Shows.objects.filter(genre="Comedy").order_by("-id")
#     return render(request, "shows_all.html", {"shows": queryset})
#
#
# def tv_show_fantasy(request):
#     queryset = models.Shows.objects.filter(genre="Fantasy").order_by("-id")
#     return render(request, "shows_all.html", {"shows": queryset})
#
#
# def tv_show_sci_fi(request):
#     queryset = models.Shows.objects.filter(genre="Sci-Fi").order_by("-id")
#     return render(request, "shows_all.html", {"shows": queryset})
#
#
# def tv_show_onime(request):
#     queryset = models.Shows.objects.filter(genre="Anime").order_by("-id")
#     return render(request, "shows_all.html", {"shows": queryset})
#
#
# def tv_show_romantic(request):
#     queryset = models.Shows.objects.filter(genre="Romantic").order_by("-id")
#     return render(request, "shows_all.html", {"shows": queryset})
#
#
# def tv_show_action(request):
#     queryset = models.Shows.objects.filter(genre="Action").order_by("-id")
#     return render(request, "shows_all.html", {"shows": queryset})


class TVShowDetailView(generic.DetailView):
    template_name = "shows_detail.html"

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.Shows, id=show_id)

# def get_show_detail(request, id):
#     object = get_object_or_404(models.Shows, id=id)
#     return render(request, "shows_detail.html", {"show": object})


class TVShowCreateView(generic.CreateView):
    template_name = "add_shows.html"
    form_class = forms.TVShowForm
    queryset = models.Shows.objects.all()
    success_url = "/shows/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(TVShowCreateView, self).form_valid(form=form)

# def add_show(request):
#     method = request.method
#     if method == "POST":
#         form = forms.TVShowForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # return HttpResponse("TVShow Created successfully")
#             return redirect(reverse("shows_url:shows_all_url"))
#     else:
#         form = forms.TVShowForm()
#     return render(request, "add_shows.html", {"form": form})


class TVShowUpdateView(generic.UpdateView):
    template_name = "show_update.html"
    form_class = forms.TVShowForm
    success_url = "/shows/"

    def get_object(self, **kwargs):
        show_id = self.kwargs.get("id")
        return get_object_or_404(models.Shows, id=show_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(TVShowUpdateView, self).form_valid(form=form)


# def show_update(request, id):
#     show_object = get_object_or_404(models.Shows, id=id)
#     if request.method == "POST":
#         form = forms.TVShowForm(instance=show_object, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("shows_url:shows_all_url"))
#     else:
#         form = forms.TVShowForm(instance=show_object)
#     return render(request, "show_update.html", {"form": form,
#                                                 "object": show_object})

class TVShowsDeleteView(generic.DeleteView):
    success_url = "/shows/"
    template_name = "confirm_delete_show.html"

    def get_object(self, **kwargs):
        shows_id = self.kwargs.get('id')
        return get_object_or_404(models.Shows, id=shows_id)


# def show_delete(request, id):
#     show_object = get_object_or_404(models.Shows, id=id)
#     show_object.delete()
#     return redirect(reverse("shows_url:shows_all_url"))
