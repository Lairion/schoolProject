from django.db import models

# Create your models here.
class SchoolClass(models.Model):
    """
    Description: Model Description
    """
    number = models.IntegerField()
    alfa = models.CharField(max_length=50)

    def __str__(self):
        return '%s%s'%(self.number,self.alfa) 
    
    class Meta:
        pass

class Pupil(models.Model):
    """
    Description: Model Description
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    in_class = models.ForeignKey('SchoolClass', 
        on_delete=models.CASCADE,
    	null=True,
    	blank=True, 
    	related_name='in_class')

    def __str__(self):
        return '%s %s' % (self.first_name,self.last_name)
    

    class Meta:
        pass