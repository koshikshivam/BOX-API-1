from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Box(models.Model): 
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    length = models.FloatField(null=True,blank=True,default=0.0)
    width = models.FloatField(null=True,blank=True,default = 0.0)
    height = models.FloatField(null = True,blank=True,default = 0.0)
    displayfield = ['length','width','height','area','vol']    


    @property
    def vol(self):
        vol = (self.length*self.width*self.height)
        return vol
    
    @property
    def area(self):
        area= (2*self.length*self.width + 2*self.length*self.height + 2*self.height*self.width)
        return area
    
    
    
        
