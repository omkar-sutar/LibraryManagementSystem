from datetime import datetime, timedelta
from django.utils import timezone
import django
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import check_password
import cv2
from . import utilities
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

def landingpage(request):
    return render(request, 'library/landingPage.html')


@login_required
def homePage(request,books=None):
    return render(request, 'library/homePage.html')


def teamPage(request):
    return render(request, 'library/teamPage.html')


@login_required
def search(request):
    query = request.GET["booksearch"]
    allBooks = models.Book.objects.all()
    print(allBooks, " all books")
    resultBooks = []
    matchedBooks = dict()
    for book in allBooks:
        if book.available == False:
            continue
        cnt = 0
        query_words = query.split(' ')
        for word in query_words:
            if word.lower() in book.name.lower():
                cnt += 1
        if book.name not in matchedBooks:
            resultBooks.append([cnt, book])
            matchedBooks[book.name] = 1
    resultBooks = sorted(resultBooks, key=lambda cnt_book: -cnt_book[0])
    print(resultBooks)
    if len(resultBooks) > 5:
        resultBooks[:] = resultBooks[:5]
    books = []
    for cnt_book in resultBooks:
        books.append([str(cnt_book[1]).rsplit(' ')[0], cnt_book[1].barcode])
    print(books)
    return redirect('library:homePage', books)


# @login_required
def rent(request, barcode):
    book = models.Book.objects.get(barcode=barcode)
    # mark book as unavailable
    book.available = False
    book.save()
    # add book in active_rented_books, rental_history
    member = models.Member.objects.get(user=request.user)
    status = 1
    expected_return_date = timezone.now() + timedelta(7)
    active_rented_book = models.Active_Rented_Books(book=book, member=member, status=status,
                                                    expected_return_date=expected_return_date)
    active_rented_book.save()
    rented_book = models.Rental_History(book=book, member=member, status=status,
                                        expected_return_date=expected_return_date)
    rented_book.save()
    messages.success(request, f"Book Rented Successfully!")
    return redirect('library:homePage')


@login_required
def return_book_superuser(request, barcode, prn):
    if request.user.is_superuser == False:
        return HttpResponse("Unauthorized access: Please continue with superuser account")
    book = models.Book.objects.get(barcode=barcode)
    rented_book = models.Active_Rented_Books.objects.get(book=book)
    member = models.Member.objects.get(prn=prn)
    # check for late return
    if rented_book.expected_return_date < timezone.now():
        # get original cost
        fine_l = models.Fine.objects.filter(member=member)
        if len(fine_l) == 0:
            fine = models.Fine(member=member, amount=50)
            fine.save()
        else:
            fine = fine_l[0]
            fine.amount += 50
            fine.save()
    book.available = True
    book.save()
    rented_book.delete()
    rent_history = models.Rental_History.objects.get(book=book, status=1)
    rent_history.status = 0
    rent_history.return_date = timezone.now()
    rent_history.save()
    return HttpResponse("Done")


class Login(View):

    def get(self, request, template_name='library/loginPage.html'):
        return render(request, template_name)

    def post(self, request, template_name='library/loginPage.html'):
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


class Register(View):

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
                user = User.objects.create_user()
                return redirect('Login')

        else:
            args["error_message"] = "Passwords Don't Match. Please Try Again."
            return render(request, template_name, args)


class uploadBarcode(View):
    def get(self, request):
        if not request.user:
            return redirect('Login')
        return render(request, 'library/simple_upload.html')

    def post(self, request):
        if not request.user:
            return redirect('Login')
        myfile = request.FILES['myfile']
        print(1)
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        img = cv2.imread(filename)
        res = utilities.decode(img)
        # TODO
        if not res:
            return HttpResponseBadRequest()
        barcode = res["data"]
        messages.success(request, f"Book Rented Successfully!")
        return redirect('library:rent', barcode)


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
