from django.db import models  
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    eaddress = models.CharField(max_length=250) 
    edesignation = models.CharField(max_length=200) 
    class Meta:  
        db_table = "employee" 
