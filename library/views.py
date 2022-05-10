
from django.contrib.auth.models import User
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.hashers import check_password

# Create your views here.

class landingPage(View):

    def get(self, request, template_name='landingPage.html'):
        return render(request, template_name)


class Login(View):

    def get(self, request, template_name='login.html'):
        return render(request, template_name)

    def post(self, request, template_name='login.html'):
        prn = request.POST['prn']
        password = request.POST['password']

        user = authenticate(prn=prn, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            args = {}
            args["error_message"] = "Invalid Credentials. Please Try Again."
            return render(request, template_name, args)


class register(View):

    def get(self, request, template_name='register.html'):
        return render(request, template_name)

    def post(self, request, template_name='register.html'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        prn = request.POST['prn']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        args = {}

        if password1 == password2:
            if User.objects.filter(prn=prn).exists():
                args["error_message"] = "PRN Already Exists. Please Try Again."
                return render(request, template_name, args)
            elif User.objects.filter(email=email).exists():
                args["error_message"] = "Email Already Exists. Please Try Again."
                return render(request, template_name, args)
            else:
                return redirect('Login')

        else:
            args["error_message"] = "Passwords Don't Match. Please Try Again."
            return render(request, template_name, args)


def Logout(request):
    logout(request)
    return redirect('/')

class viewProfile(View):
    def get(self, request, template_name="viewProfile.html"):
        if request.user:
            return render(request, template_name)
        else:
            return render(request, "login.html")

# Change password
class resetPassword(View):

    def get(self, request, template_name="changepassword.html"):
        return render(request, template_name)

    def post(self, request, template_name="changepassword.html"):
        currPassword = request.POST.get('currentPassword')
        newPassword = request.POST.get('newPassword')
        confPassword = request.POST.get('reNewPassword')

        try:
            matchcheck = check_password(currPassword, request.user.password)
            if matchcheck is False:
                err = {}
                err["error_message"] = "Entered Current Password is Incorrect. Please Retry."
                return render(request, template_name, err)
            if newPassword != confPassword:
                err = {}
                err["error_message"] = "Entered New Passwords don't Match. Please Retry."
                return render(request, template_name, err)
        except:
            err = {}
            err["error_message"] = "Refresh the Page to change the Password Again."
            return render(request, template_name, err)

        # U = User.objects.get(username=request.user.username)
        U = request.user
        U.set_password(newPassword)
        U.save()
        update_session_auth_hash(request, U)
        err = {}
        
        err["error_message"] = "Password changed successfully."
        return render(request, 'viewProfile.html')