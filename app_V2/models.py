from django.db import models

# Create your models here.
class statusclass(models.Model):
    status = models.CharField(max_length=20,unique=True)
    
    def __str__(self):
        return self.status
    
class userModel(models.Model):
    name = models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.name

class AttendanceRecord(models.Model):
    name = models.ForeignKey(to=userModel,on_delete=models.CASCADE)
    date = models.DateField()
    status = models.ForeignKey(to=statusclass,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name.name + '_' + self.date.strftime('%d/%m/%Y')
