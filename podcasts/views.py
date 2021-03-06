from django.shortcuts import get_object_or_404, render
from .models import Podcast

def index(request):
    podcasts_list = Podcast.objects.all()
    return render(request, 'podcasts/index.html', {"podcasts" : podcasts_list})

def detail(request, podcast_id):
    podcast =  get_object_or_404(Podcast, pk=podcast_id)
    return render(request,'podcasts/detail.html',{'podcast':podcast})
