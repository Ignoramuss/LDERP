from django.db import models
from datetime import date

# Create your models here.

#Model of the students
class Student_info(models.Model):
    #Personal information
    stud_name = models.CharField(max_length = 200)
    stud_school = models.CharField(max_length = 200)
    stud_standard = models.CharField(max_length = 30)
    stud_div = models.CharField(max_length = 30)
    date_of_fill = models.DateField()
    date_of_birth = models.DateField()
    #Guardian information
    #Father
    father_name = models.CharField(max_length=200)
    father_contact = models.BigIntegerField()
    father_email = models.EmailField(max_length = 200)
    father_education = models.CharField(max_length=200)
    father_occupation = models.CharField(max_length=200)
    #Mother
    mother_name = models.CharField(max_length=200)
    mother_contact = models.BigIntegerField()
    mother_email = models.EmailField(max_length = 200)
    mother_education = models.CharField(max_length=200)
    mother_occupation = models.CharField(max_length=200)
    #Academic info
    stud_grades = models.TextField()

class language_disabilities(models.Model):
    dis_name = models.CharField(max_length=200)
    student = models.ForeignKey(Student_info, on_delete=models.CASCADE)

class mathematical_disabilities(models.Model):
    dis_name = models.CharField(max_length=200)
    student = models.ForeignKey(Student_info, on_delete=models.CASCADE)

class parent_awareness(models.Model):
    awareness_type= models.CharField(max_length=200)
    awareness_score= models.IntegerField()
    student = models.ForeignKey(Student_info, on_delete=models.CASCADE)
