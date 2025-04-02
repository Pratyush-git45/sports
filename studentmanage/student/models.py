from django.db import models

class Student(models.Model):
  first_name = models.CharField(max_length=100)
  lastname_name = models.CharField(max_length=100)
  email = models.EmailField(unique= True)
  phone_no = models.CharField(max_length=10)
  student_id = models.CharField(max_length=20, unique=True)

  def __str__(self):
    return f"{self.first_name} {self.lastname_name} {self.student_id}"

class Sport(models.Model):
  sport_name = models.CharField(max_length=100)
  sport_id = models.CharField(max_length=20, unique=True)

  def __str__(self):
    return f"{self.sport_name} - {self.sport_id}"


class Enrollment(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
  enrollment_data= models.DateField(auto_now_add=True)

  def __str__(self):
    return f"{self.student.first_name} enrolled in {self.sport.sport_name}"
# Create your models here.
