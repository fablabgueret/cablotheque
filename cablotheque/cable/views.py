from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from .models import Cable

def index(request):
    return HttpResponse("Hi Pepito")


class CableListView(ListView):
    model = Cable
    def get_context_data(self, **kwargs):
        context = super(CableListView, self).get_context_data(**kwargs)
        return context
