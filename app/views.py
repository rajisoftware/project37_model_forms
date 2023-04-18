from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import *
def insert_Topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        To=Topic.objects.get_or_create(topic_name=tn)[0]
        To.save()
        return HttpResponse(f'the data submited {tn}')
    return render(request,'insert_Topic.html')
def insert_Webpage(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    if request.method=='POST':
        topic=request.POST['topic']
        name=request.POST.get('name')
        url=request.POST['url']
        email=request.POST['email']
        To=Topic.objects.get(topic_name=topic)
        To.save()
        Wo=Webpage.objects.get_or_create(topic_name=To,name=name,url=url,mail=email)[0]
        Wo.save()
        return HttpResponse('Webpages inserted successfully')
    return render(request,'insert_Webpage.html',d)
def insert_Access(request):
    LOW=Webpage.objects.all()
    d={'webpages':LOW}
    if request.method=='POST':
        name=request.POST['name']
        author=request.POST['author']
        date=request.POST['date']
        Wo=Webpage.objects.get(name=name)
        Wo.save()
        Ao=AccessRecord.objects.get_or_create(name=Wo,author=author,date=date)[0]
        Ao.save()
        return HttpResponse('Access records inserted successfully')
    return render(request,'insert_Access.html',d)
def retrieve_data(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    if request.method=='POST':
        td=request.POST.getlist('topic')
        print(td)
        webqueryset=Webpage.objects.none()
        for i in td:
            webqueryset=webqueryset|Webpage.objects.filter(topic_name=i)
            d1={'webpages':webqueryset}
        return render(request,'display_Webpage.html',d1)
    return render(request,'retrieve_data.html',d)
def chekbox(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'chekbox.html',d)
def radio_type(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'radio_type.html',d)