from django.db import models

# Create your models here.



class hospital(models.Model):
    status_choice=(('accepted','accepted'),('rejected','rejected'),('pending','pending'))
    Hospital_name = models.CharField(max_length=200)
    phone_no = models.IntegerField(unique=True)
    Email_id  = models.CharField(max_length=200,unique=True)
    location = models.CharField(max_length=200)
    password = models.CharField(max_length=200,null=True,blank=True)
    status=models.CharField(choices=status_choice,default='pending',max_length=200)
    def __str__(self):
        return self.Hospital_name


class receiver(models.Model):
    status_choice=(('accepted','accepted'),('rejected','rejected'),('pending','pending'))
    name = models.CharField(max_length=200)
    phone_no = models.IntegerField(unique=True)
    Email_id = models.CharField(max_length=200,unique=True)
    Address = models.CharField(max_length=200)
    hospital_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200,null=True,blank=True)
    status=models.CharField(choices=status_choice,default='pending',max_length=200)
    def __str__(self):
        return self.name


class donor(models.Model):
    hospital_id  = models.ForeignKey(hospital, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    doctername = models.CharField(max_length=200)
    Organ_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200,null=True,blank=True)
    age = models.CharField(max_length=200)
    bloodgroup = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    photo = models.FileField()
    idproof = models.FileField()
    def __str__(self):
        return self.name


class Request(models.Model):
    status_choice=(('accepted','accepted'),('Assigned','Assigned'),('pending','pending'))
    reciver_id = models.ForeignKey(receiver, on_delete=models.CASCADE,null=True,blank=True)
    hospital_id = models.ForeignKey(hospital, on_delete=models.CASCADE,null=True,blank=True)
    donor_id = models.ForeignKey(donor,on_delete=models.CASCADE,null=True,blank=True)
    organ_name = models.CharField(max_length=200,null=True,blank=True)
    certificate = models.CharField(max_length=200,null=True,blank=True)
    status=models.CharField(choices=status_choice,default='pending',max_length=200)
    def __str__(self):
        return self.reciver_id.name
