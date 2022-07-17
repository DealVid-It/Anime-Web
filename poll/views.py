from django.shortcuts import render
from .models import Poll


def poll_view(request):
    return render(request, "poll.html", {})


def thanks_view(request):
    if(request.method == 'POST'):
        name = request.POST.get('name')
        anime = request.POST.get('anime')
        subORdub = request.POST.get('subORdub')
        if name == "" or anime == "":
            return render(request, "invalid.html", {})
        new_entry = Poll(name=name, anime=anime, subORdub=subORdub)
        new_entry.save()
    return render(request, "thanks.html", {})
