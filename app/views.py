from django.shortcuts import render
from app.models import *

# Create your views here.
def topic(request):
     LOT=TOPIC.objects.all()
     d={'topic':LOT}
     return render(request,'topic.html',context=d)

def webpage_list(request):
     web=Webpages.objects.all()
     context={'web':web}
     return render(request,'webpage.html',context)
