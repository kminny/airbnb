from django.shortcuts import render
from django.utils import timezone
from django.views.generic import DetailView, ListView
from django_countries import countries
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context


class RoomDetail(DetailView):

    """ RoomDetail Definition """

    model = models.Room


def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))
    room_types = models.RoomType.objects.all()

    form = {
        "city": city,
        "s_country": country,
        "s_room_type": room_type,
    }

    choices = {
        "countries": countries,
        "room_types": room_types,
    }

    return render(
        request,
        "rooms/search.html",
        {**form, **choices},
    )
