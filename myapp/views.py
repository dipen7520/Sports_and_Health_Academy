from django.shortcuts import render ,redirect ,HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from .models import Contacts
import random

# Create your views here.
def homepage(request):
    contact= Contacts()
    if request.method== "POST": 
        contact.name= request.POST['name']
        contact.email= request.POST['email']
        contact.phoneno= request.POST['phone_no']
        contact.textmsg= request.POST['textmsg']
        contact.save()
        return redirect('homepage')
    return render(request,'Indexpage/index.html')

def create_otp():
    no = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    otp = ""
    for i in range(6):
        otp += str(random.choice(no))
        print(otp)
    return otp

def register(request):
    if request.method == "POST":
        fname= request.POST['fname']
        lname= request.POST['lname']
        email= request.POST['eml']
        uname= request.POST['uname']
        password= request.POST['pass']
        conpass= request.POST['conpass']

        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email already Exist!!')
            return redirect('register')
        elif User.objects.filter(username=uname).exists():
            messages.info(request, 'username already Exist!!')
            return redirect('register')
        else:
            if password != conpass:
                messages.info(request, 'Password does not match!!!')
                return redirect('register')
            else:
                user= User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=password)
                    
                #email sent
                otp = create_otp()
                subject = 'BRUTAL Sports Academy'
                message = f"Your OTP for Verification is-{otp}.\n\nNote:- Don't share your OTP with anyone.\n\nFrom:- BRUTAL Sports Academy"
                email_from = settings.EMAIL_HOST_USER
                email_to = email

                #send_mail('subject', 'body', 'sender mail', 'receiver mail')
                send_mail(subject, message, email_from, [email_to], fail_silently=False)

                #user save
                user.save()

                #session
                request.session['otp'] = otp
                
                return redirect('otpcheck')
    else:
        return render(request , 'register.html')

def otpcheck(request):
    if 'otp' in request.session.keys():
        if request.method == 'POST':
            otp = request.POST['otp']
            if request.session['otp'] == otp:
                del request.session['otp']
                return redirect('login')
            else:
                messages.info(request, 'OTP is Invalid')
                return render(request, 'Dashboard/otp_check.html')
        return render(request, 'Dashboard/otp_check.html')
    else:
        return render(request, 'Dashboard/otp_check.html')

def login(request):
    if request.method == "POST":
        uname= request.POST['uname']
        password= request.POST['pass']

        user= auth.authenticate(username=uname,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request, 'username/password invalid!!!')
            return redirect('login')
    else:
        return render(request, 'login.html')

def forget_password(request):
    return render(request, 'Dashboard/forget_password.html')

def forget_password_email_form(request):
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            #email sent
            otp = create_otp()
            subject = 'Eshop India Company'
            message = f"Your OTP for Verification is-{otp}.\n\nNote:- Don't share your OTP with anyone.\n\nFrom:- Eshop India Company"
            email_from = settings.EMAIL_HOST_USER
            email_to = email

            #send_mail('subject', 'body', 'sender mail', 'receiver mail')
            send_mail(subject, message, email_from, [email_to], fail_silently=False)

            #session
            request.session['otp'] = otp
            return render(request, 'Dashboard/forget_password_form.html', {'email' : email})
        else:
            messages.info(request, 'Email is Not Registered Yet!!')
            return render(request, 'Dashboard/forget_password.html', {'email' : email})
    else:
        return render(request, 'Dashboard/forget_password.html')

def forget_password_form(request):
    if 'otp' in request.session.keys():
        if request.method == 'POST':

            email = request.POST['email']
            new_pass = request.POST['new_pass']
            confirm_pass = request.POST['confirm_pass']
            otp = request.POST['otp']

            if request.session['otp'] == otp:
                if new_pass == confirm_pass:
                    del request.session['otp']

                    user = User.objects.get(email=email)
                    user.password = make_password(new_pass)
                    user.save()
                    return render(request, 'login.html')
                else:
                    messages.info(request, 'Password and Confirm Password not matched!!')
                    return render(request, 'Dashboard/forget_password_form.html', {'otp' : otp, 'email' : email})

            else:
                messages.info(request, 'OTP is Invalid')
                return render(request, 'Dashboard/forget_password_form.html', {'otp' : otp, 'email' : email})    
    else:
        return render(request, 'Dashboard/forget_password_form.html')


def logout(request):
    auth.logout(request)
    return redirect('homepage')

def dashboard(request):
    if request.user.is_authenticated:
        context = {'text':'about'}
        return render(request, 'Dashboard/dashboard.html', context)
    else:
        return render(request, 'login.html')

        
def service(request):
    context = {'text':'service'} 
    return render(request, 'Dashboard/service.html', context)
def reg(request):
    return render(request, 'Dashboard/reg.html')
def history(request):
    context = {'text':'history'} 
    return render(request, 'Dashboard/history.html', context)
def profile(request):
    context = {'text':'profile'} 
    return render(request, 'Dashboard/profile.html', context)
def trainer(request):
    context = {'text':'trainer'} 
    return render(request, 'Dashboard/trainer.html', context)
def contact(request):
    contact= Contacts()
    if request.method== "POST": 
        contact.name= request.POST['name']
        contact.email= request.POST['email']
        contact.phoneno= request.POST['phone_no']
        contact.textmsg= request.POST['textmsg']
        contact.save()
        return redirect('dashboard')
    context = {'text':'contact'} 
    return render(request, 'Dashboard/contact.html', context)
def plan(request):
    context = {'text':'plan'} 
    return render(request, 'Dashboard/plan.html', context)