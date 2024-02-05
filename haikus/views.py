from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect

from .models import Haiku, Tag, Tanka
from .forms import TankaForm


class HaikuList(generic.ListView):
    """
    Renders all objects of Haiku model as list
    """

    queryset = Haiku.objects.order_by("-create_date")
    template_name = "haikus/index.html"
    paginate_by = 6

    def get_context_data(self, *args, **kwargs):
        tag_items = Tag.objects.all()
        context = super(HaikuList, self).get_context_data(*args, **kwargs)
        context["tag_items"] = tag_items
        return context


class HaikuDetail(View):
    """
    Haiku detail view renders all data about haiku entry
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Haiku.objects
        haiku = get_object_or_404(queryset, slug=slug)
        tankas = haiku.tankas.order_by("create_date")
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
                "tanka_form": TankaForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Haiku.objects
        haiku = get_object_or_404(queryset, slug=slug)
        tankas = haiku.tankas.order_by("create_date")
        liked = False
        if haiku.likes.filter(id=self.request.user.id).exists():
            liked = True

        tanka_form = TankaForm(data=request.POST)

        if tanka_form.is_valid():
            tanka_form.instance.email = request.user.email
            tanka_form.instance.name = request.user.username
            tanka = tanka_form.save(commit=False)
            tanka.post = haiku
            tanka.save()
        else:
            tanka_form = TankaForm()

        return render(
            request,
            "haiku_detail.html",
            {
                "haiku": haiku,
                "tankas": tankas,
                "tanka_added": True,
                "liked": liked,
                "tanka_form": tanka_form,
            },
        )


class HaikuLike(View):
    """
    Allows user to like/unlike haikus
    """

    def post(self, request, slug):
        haiku = get_object_or_404(Haiku, slug=slug)

        if haiku.likes.filter(id=request.user.id).exists():
            haiku.likes.remove(request.user)
        else:
            haiku.likes.add(request.user)

        return HttpResponseRedirect(reverse("haiku_detail", args=[slug]))
