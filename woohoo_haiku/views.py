from django.shortcuts import render


def handler404(request, exception):
    """
    renders custom 404 page
    """
    return render(request, "errors/404.html", status=404)


def handler500(request):
    """
    renders custom 500 page
    """
    return render(request, "errors/500.html", status=500)
