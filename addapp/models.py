from django.db import models

class Register(models.Model):
  emailid= models.CharField(max_length=200)
  password= models.CharField(max_length=200)
  mobile= models.CharField(max_length=200)
  fullname= models.CharField(max_length=200)
  def __str__(self):
  	return "emailid is "+self.emailid +" password is "+self.password +" mobile is "+self.mobile+" fullname is "+self.fullname