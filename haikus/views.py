from django.shortcuts import render, get_object_or_404
from django.views import generic, View

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


class HaikuDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Haiku.objects
        haiku = get_object_or_404(queryset, slug=slug)
        tankas = haiku.tankas.order_by('create_date')
        liked = False
        if haiku.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "haikus/haiku_detail.html",
            {
                "haiku": haiku,
                "tankas": tankas,
                "tanka_added": False,
                "liked": liked,
                # add tanka form variable
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Haiku.objects
        haiku = get_object_or_404(queryset, slug=slug)
        tankas = haiku.tankas.order_by('create_date')
        liked = False
        if haiku.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "haiku_detail.html",
            {
                "haiku": haiku,
                "tankas": tankas,
                "tanka_added": True,
                "liked": liked,
                # add tanka form variable
            },
        )