from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    prn = models.CharField(max_length=15)
    email = models.EmailField(max_length=200)
    #avatar = models.ImageField(default = 'avatar.png', upload_to='avatars/')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    #Choices for branch
    ELECTRONICS="ELN"
    ELECTRICAL="ELE"
    MECHANICAL="MECH"
    INFORMATION_TECHNOLOGY="IT"
    COMPUTER_SCIENCE="CS"
    CIVIL="CVL"
    BRANCH_CHOICES=[
        (ELECTRONICS,"Electronics"),
        (ELECTRICAL,"Electrical"),
        (MECHANICAL,"Mechanical"),
        (INFORMATION_TECHNOLOGY,"Information Technology"),
        (COMPUTER_SCIENCE,"Computer Science"),
        (CIVIL,"Civil")
    ]
    branch=models.CharField(max_length=50,choices=BRANCH_CHOICES)

    #Degree choices
    DIPLOMA="DP"
    BTECH="BT"
    MTECH="MT"
    DEGREE_CHOICES=[
        (DIPLOMA,"Diploma"),
        (BTECH,"B. Tech."),
        (MTECH,"M. Tech.")
    ]
    degree=models.CharField(max_length=50,choices=DEGREE_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name} -{self.created.strftime('%d-%m-%Y')}"


class Category(models.Model):
    id=models.AutoField(primary_key=True)
    branch_name=models.CharField(max_length=50)

class Rack(models.Model):
    id=models.AutoField(primary_key=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    rack_num=models.IntegerField()

class Book(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,null=False)
    author=models.CharField(max_length=50,null=False)
    edition=models.CharField(max_length=50,null=False)
    category=models.ForeignKey(Category,null=False,on_delete=models.CASCADE)
    available=models.BooleanField(null=False)

    def __str__(self) -> str:
        return f"{self.name}"

class Rental_History(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    member=models.ForeignKey(Member,on_delete=models.DO_NOTHING)
    status=models.IntegerField(null=False)
    date=models.DateTimeField(auto_now_add=True)
    expected_return_date=models.DateTimeField(null=False)

class Active_Rented_Books(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    member=models.ForeignKey(Member,on_delete=models.CASCADE)
    status=models.IntegerField(null=False)
    date=models.DateTimeField(auto_now_add=True)
    expected_return_date=models.DateTimeField(null=False)

class Fine(models.Model):
    member=models.ForeignKey(Member,on_delete=models.CASCADE)
    amount=models.FloatField(default=0,null=False)

class Transaction_History(models.Model):
    id=models.AutoField(primary_key=True)
    member=models.ForeignKey(Member,on_delete=models.CASCADE)
    amount=models.FloatField(null=False)
    date=models.DateTimeField(auto_now_add=True)

