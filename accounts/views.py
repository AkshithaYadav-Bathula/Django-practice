from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def login(request):
    if request.method == "POST":
        username=request.POST['username']
        p = request.POST['password']
        user = auth.authenticate(username=username,password = p)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')    
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    # render()
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['user_name']
        email = request.POST['email']
        p1 = request.POST['password1']
        p2 = request.POST['password2']
        #TO VERIFY PW AND NO DUPLICATE EMAIL 
        if p1 == p2:
            if User.objects.filter(username = username).exists():
                # print("Username taken")
                messages.info(request,'Username taken')
            elif User.objects.filter(email=email).exists():
                # print("email taken")
                messages.info(request,'Email taken')
            else:
                user = User.objects.create_user(username=username, password = p1, email = email, first_name = first_name, last_name = last_name)
                user.save()
                messages.info(request,'user created')
                # print('user created')
                return redirect('login')
              
        else:
            # print('Password not matching')
            messages.info(request,'Password not matching')
        

    return render(request,'register.html')