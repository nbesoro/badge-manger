from django.shortcuts import render


# Create your views here.
def index(request):

    return render(request, "index.html", {})


def profil(request):

    return render(request, "profile.html", {})


def detail(request):

    return render(request, "detail.html", {})
