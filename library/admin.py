from django.contrib import admin
from .models import Active_Rented_Books, Book, Category, Fine, Member, Rack, Rental_History, Transaction_History

# Register your models here.
admin.site.register(Member)
admin.site.register(Category)
admin.site.register(Rack)
admin.site.register(Book)
admin.site.register(Rental_History)
admin.site.register(Active_Rented_Books)
admin.site.register(Fine)
admin.site.register(Transaction_History)

