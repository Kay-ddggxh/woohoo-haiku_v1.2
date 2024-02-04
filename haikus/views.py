from django.shortcuts import render
from django.views import generic

from .models import Haiku, Tag, Tanka


class HaikuList(generic.ListView):
    """
    Renders all objects of Haiku model as list
    """
    queryset = Haiku.objects.order_by('-create_date')
    template_name = "haikus/index.html"
    paginate_by = 6

    def get_context_data(self, *args, **kwargs):
        tag_items = Tag.objects.all()
        context = super(HaikuList, self).get_context_data(*args, **kwargs)
        context["tag_items"] = tag_items
        return context