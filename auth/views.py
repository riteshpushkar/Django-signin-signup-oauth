
from email import message
from imaplib import _Authenticator
from pdb import post_mortem
from telnetlib import LOGOUT
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# def docpat(request):
#     if request.method == "POST" :
#         doc = request.POST.get('doc')
#         pat = request.POST.get('pat')
       

#         myuser = User.objects.create_user()
#         myuser.doc = doc
#         myuser.pat = pat
       
#         myuser.save()




#         messages.success(request, "Your account has been successfully created")

#         return redirect('home')




#     return render(request, "home")





def home(request):
    return render(request,"auth/index.html")
    

def signup(request) :
    if request.method == "POST" :
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        profilepic = request.POST.get('profilepic')

        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        line1 = request.POST.get('line1')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')

        if pass1 != pass2:
            messages.error(request,"passwords did not match")

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.profile_pic = profilepic
        myuser.line1 = line1
        myuser.city = city
        myuser.state = state
        myuser.pincode = pincode

        myuser.save()




        messages.success(request, "Your account has been successfully created")

        
        
        return redirect('signInform')




    return render(request, "auth/signUpform.html")


def signin(request) :

   








    if request.method == "POST" :
        username = request.POST['username']
        pass1 = request.POST['pass1']


        user = authenticate(username=username, password=pass1)

        if user is not None :
            login(request, user)
            fname = user.first_name
            lname = user.last_name
            email = user.email
            # city = user.city
            # state = user.state
            # pincode = user.pincode
            # profilepic = user.image
            username = user.username
            return render(request, "auth/index.html", {'fname' : fname,'username':username,'lname':lname,'email': email})

        else:
            messages.error(request, "add credentials first")
            return redirect('home')






        

        






    return render(request, "auth/signInform.html")
    


def signout(request) :
    logout(request)
    messages.success(request, "Logged out Successfully!!!")
    return redirect('home')