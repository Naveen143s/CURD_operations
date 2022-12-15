from django.shortcuts import render
from django.db.models.functions import Length

# Create your views here.
from app.models import *
def display_topic(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}

    return render(request,'display_topic.html',d)





def display_webpage(request):
    LTO=Webpage.objects.all()
    LTO=Webpage.objects.filter(Topic_name='cricket')
    LTO=Webpage.objects.order_by('name')
    LTO=Webpage.objects.order_by('-name')
    LTO=Webpage.objects.order_by(Length('name'))
    LTO=Webpage.objects.order_by(Length('name').desc())
    LTO=Webpage.objects.exclude(name='msd')
    LTO=Webpage.objects.order_by('-name')
    
    d={'LTO':LTO}
    return render(request,'display_webpage.html',d)
