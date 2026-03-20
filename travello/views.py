from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    # return HttpResponse("Hello World")
    
    # return render(request,'home.html', {'name':'Akshitha'})
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc='The city that never sleeps'
    dest1.price = 999
    # return render(request,'index.html', {'price':700}) 
    return render(request, 'index.html', {'dest1':dest1})
#send req in rsponse