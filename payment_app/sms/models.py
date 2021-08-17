from django.db import models

# Create your models here.

class customer(models.Model):
    email = models.EmailField(max_length=40,unique = True)
    firstName = models.CharField(max_length=40, blank=True, null=True)
    lastName = models.CharField(max_length=40, blank=True, null =True)

    def __str__(self):
        return(str(self.email))    

class documents(models.Model):
    email = models.OneToOneField(customer, on_delete=models.CASCADE)
    poi = models.ImageField(upload_to = "sms/images/", blank = True, null = True)
    poaFront = models.ImageField(upload_to = "sms/images/", blank = True, null = True)
    poaBack = models.ImageField(upload_to = "sms/images/", blank = True, null = True)
    bankProof = models.ImageField(upload_to = "sms/images/", blank = True, null = True)
    livePic = models.ImageField(upload_to = "sms/images/", blank = True, null = True)
    loanAgreement = models.ImageField(upload_to = "sms/images/", blank = True, null = True)
    nachMandate = models.ImageField(upload_to = "sms/images/", blank = True, null = True)
    

    def __str__(self):
        return(str(self.email))

class statements(models.Model):
    email = models.OneToOneField(customer, on_delete=models.CASCADE)
    statementPageOne = models.ImageField(upload_to = "sms/images/", blank = True, null = True)
    statementPageTwo = models.ImageField(upload_to = "sms/images/", blank = True, null = True)
    statementPageThree = models.ImageField(upload_to = "sms/images/", blank = True, null = True)
    loanStatus = models.CharField(max_length=10,  blank = True, null = True)

    def __str__(self):
        return(str(self.email))
        

