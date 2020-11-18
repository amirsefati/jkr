from django.db import models

# Create your models here.
class Archive(models.Model):
    Ta1    = models.CharField(max_length=150)
    Ta2    = models.CharField(max_length=150,null=True,blank=True)
    Ta3    = models.CharField(max_length=150,null=True,blank=True)
    Ta4    = models.CharField(max_length=150,null=True,blank=True)

    C12Na  = models.CharField(max_length=200,null=True,blank=True)
    C5Na   = models.CharField(max_length=200,null=True,blank=True)
    NLSh   = models.CharField(max_length=200,null=True,blank=True)
    C4Sh   = models.CharField(max_length=200,null=True,blank=True)
    NSh    = models.CharField(max_length=200,null=True,blank=True)
    NaF    = models.CharField(max_length=200,null=True,blank=True)
    Na30F  = models.CharField(max_length=200,null=True,blank=True)
    C12Sh  = models.CharField(max_length=200,null=True,blank=True)
    B      = models.CharField(max_length=200,null=True,blank=True)
    CTa    = models.CharField(max_length=200,null=True,blank=True)
    CGI    = models.CharField(max_length=200,null=True,blank=True)
    GI     = models.CharField(max_length=200,null=True,blank=True)
    CSGI   = models.CharField(max_length=200,null=True,blank=True)
    SGI    = models.CharField(max_length=200,null=True,blank=True)

     