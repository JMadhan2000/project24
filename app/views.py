from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
def htmlforms(request):
    if request.method=='POST':
        Tn=request.POST['tn']
        TP=Topic.objects.get_or_create(Topic_name=Tn)
        TP.save()
        return HttpResponse('Topic name created')
    return render(request,'htmlforms.html')



def htmlforms2(request):
    if request.method=='POST':
        Tn=request.POST['tn']
        TP=Topic.objects.get_or_create(Topic_name=Tn)[0]
        TP.save()
        return HttpResponse('Topic name created')

    return render(request,'htmlforms2.html')