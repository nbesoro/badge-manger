from django.shortcuts import render, get_object_or_404
from annime import models

# Create your views here.
def index(request):
    annimes = models.AnnimeVideo.objects.select_related('author').all()
    
    data = {
        "annimes": annimes
    }

    return render(request, "index.html", data)


def profil(request):

    return render(request, "profile.html", {})


def detail(request, id):
    annime = get_object_or_404(models.AnnimeVideo, pk=id)
    
    data = {
        "annime": annime
    }

    return render(request, "detail.html", data)
