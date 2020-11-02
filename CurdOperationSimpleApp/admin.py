from django.contrib import admin
from .models import Studentdatabase
# Register your models here.

class AdminStudentdatabase(admin.ModelAdmin):
    list_display = ['Roll_number','First_name','Last_name','Email','School_name','Class_name','Section_name','Telugu_marks','Hindi_marks','English_marks','Maths_marks','Science_marks','Social_marks']

admin.site.register(Studentdatabase,AdminStudentdatabase)
