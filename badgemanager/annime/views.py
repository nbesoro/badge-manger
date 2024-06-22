from django.shortcuts import render, get_object_or_404
from annime import models
from django.contrib.auth.decorators import login_required
from django.db.models import F

# Create your views here.
@login_required()
def index(request):
    annimes = models.AnnimeVideo.objects.select_related("author").all()

    data = {"annimes": annimes}

    return render(request, "index.html", data)


@login_required()
def profil(request):
    user_annimes = models.AnnimeVideo.objects.select_related("author").filter(
        author=request.user
    )

    data = {"user_annimes": user_annimes}

    return render(request, "profile.html", data)


@login_required()
def detail(request, id):
    annime = get_object_or_404(models.AnnimeVideo, pk=id)
    
    annime.number_of_views = F("number_of_views") + 1
    
    annime.save(update_fields=["number_of_views"])
    
    data = {"annime": annime}

    return render(request, "detail.html", data)
