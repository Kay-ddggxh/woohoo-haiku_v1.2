from django.shortcuts import render
from django.views import generic

from .models import Haiku


class HaikuList(generic.ListView):
    """
    Renders all objects of Haiku model as list
    """
    queryset = Haiku.objects.order_by('-create_date')
    template_name = "haikus/index.html"