from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Detailuser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    Type = models.CharField(max_length=25, choices= (('Doctor','DOCTOR'),('Patient','PATIENT')),default='Doctor')
    Specialization = models.CharField(max_length=25, choices=(('Pathologist','PATHOLOGIST'), ('Radiologist', 'RADIOLOGIST'),('Obstetrician', 'OBSTETRICIAN'),('Cardiologist','CARDIOLOGIST'),('Endocrinologist','ENDOCRINOLOGIST'),('', '---------')),null=True, blank=True)
    def save(self, *args, **kwargs):
        if self.Type == "PATIENT":
            self.Specialization = ''
            super().save(*args,**kwargs)
        else:
            super().save(*args, **kwargs)  # Call the "real" save() method.
