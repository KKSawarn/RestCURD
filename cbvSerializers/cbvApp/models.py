from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    marks = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name + self.marks

