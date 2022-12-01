from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    rate = models.IntegerField()

    def __str__(self) :
        return self.name + self.desc + self.rate