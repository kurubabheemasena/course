from django.db import models

# Create your models here.
class Course(models.Model):
    cname=models.CharField(max_length=100)
    id=models.IntegerField(primary_key=True)
    teacher=models.CharField(max_length=100)

    def __str__(self):
        return self.cname



class Student(models.Model):
    roll=models.IntegerField(primary_key=True)
    id=models.ForeignKey(Course,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    mno=models.IntegerField()

    def __str__(self):
        return self.name

            


