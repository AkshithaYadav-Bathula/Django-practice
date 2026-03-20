from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    # return HttpResponse("Hello World")
    
    # return render(request,'home.html', {'name':'Akshitha'})
    # dest1 = Destination()
    # dest1.name = 'Mumbai'
    # dest1.desc='The city that never sleeps'
    # dest1.img = '/static/images/destination_1.jpg'
    # dest1.price = 999
    # dest1.offer = False

    # dest2=Destination()
    # dest2.name = "Paris"
    # dest2.img = '/static/images/destination_2.jpg'
    # dest2.desc = "The city of Love"
    # dest2.price = 552
    # dest2.offer = True

    # dest3 = Destination()
    # dest3.name = "Switzerland"
    # dest3.img = '/static/images/destination_3.jpg'
    # dest3.desc = "The city of cold and snow"
    # dest3.price = 505
    # dest3.offer = False

    # dests = [dest1,dest2,dest3]
    # return render(request,'index.html', {'price':700}) 
    # return render(request, 'index.html', {'dest1':dest1, 'dest2':dest2, 'dest3':dest3})
    dests = Destination.objects.all() #from database it is coming
    return render(request,'index.html', {'dests':dests})
#send req in rsponse