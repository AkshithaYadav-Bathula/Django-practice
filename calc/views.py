from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    # return HttpResponse("Hello World")
    data={
        'name': 'Aksh',
        'age': 21,
        'skills': ['Java', 'Python', 'Django']
    }
    # return render(request,'home.html', {'name':'Akshitha'})
    return render(request,'home.html', data) 
#send req in rsponse

# def add(request):
#     # val1 = int(request.GET['num1'])#it is in response so get

#     # val2 = int(request.GET['num2'])
#     val1 = int(request.POST["num1"])#it is in response so get

#     val2 = int(request.POST["num2"])
#     res =val1 + val2
#     return render(request, 'result.html',{'result':res})

def add(request):
    if request.method == 'POST':
        num1 = request.POST.get("num1", "").strip()
        num2 = request.POST.get("num2", "").strip()

        if num1 == "" or num2 == "":
            return render(request, 'home.html', {'error': 'Please enter both numbers'})

        try:
            val1 = int(num1)
            val2 = int(num2)
        except ValueError:
            return render(request, 'home.html', {'error': 'Enter valid numbers only'})

        res = val1 + val2
        return render(request, 'result.html', {'result': res})

    return render(request, 'home.html')