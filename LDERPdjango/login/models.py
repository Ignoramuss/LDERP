from django.db import models
from datetime import date

# Create your models here.
class LanguageDisability(models.Model):
    disability_name = models.CharField(max_length=200)

    def __str__(self):
        return self.disability_name
    # student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)

class MathematicalDisability(models.Model):
    disability_name = models.CharField(max_length=200)

    def __str__(self):
        return self.disability_name
    # student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)

class ParentalMetric(models.Model):
    metric_name = models.CharField(max_length=200)

    def __str__(self):
        return self.metric_name

#Model of the students
class StudentInfo(models.Model):
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
    father_contact = models.CharField(max_length=10)
    father_email = models.EmailField(max_length = 200)
    father_education = models.CharField(max_length=200)
    father_occupation = models.CharField(max_length=200)
    #Mother
    mother_name = models.CharField(max_length=200)
    mother_contact = models.CharField(max_length=10)
    mother_email = models.EmailField(max_length = 200)
    mother_education = models.CharField(max_length=200)
    mother_occupation = models.CharField(max_length=200)
    #Academic info
    stud_grades = models.TextField()
    language_disabilities = models.ManyToManyField(LanguageDisability)
    mathematical_disabilities = models.ManyToManyField(MathematicalDisability)
    # parent_awareness_scores = models.OneToOneField(ParentAwarenessScore)

    def __str__(self):
        return self.stud_name

    def get_language_disabilities(self):
        return ", ".join([ld.disability_name for ld in self.language_disabilities.all()])

    def get_mathematical_disabilities(self):
        return ", ".join([md.disability_name for md in self.mathematical_disabilities.all()])

class ParentalMetricScore(models.Model):
    metric_type = models.ForeignKey(ParentalMetric)
    metric_score= models.IntegerField()
    student = models.ForeignKey(StudentInfo, null=True)