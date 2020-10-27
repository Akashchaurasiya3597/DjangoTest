from django.db import models

class Studentdatabase(models.Model):
    Roll_number = models.IntegerField()
    First_name = models.CharField(max_length=100, null=True)
    Last_name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    School_name = models.CharField(max_length=100)
    Class_name = models.CharField(max_length=100)
    Section_name = models.CharField(max_length=100)
    Telugu_marks = models.IntegerField()
    Hindi_marks = models.IntegerField()
    English_marks = models.IntegerField()
    Maths_marks = models.IntegerField()
    Science_marks = models.IntegerField()
    Social_marks = models.IntegerField()

