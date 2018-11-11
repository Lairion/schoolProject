from django.db import models
from django.urls import reverse

# Create your models here.
class Faculty(models.Model):
    """
    Description: Model Description
    """
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        pass

class LearnTable(models.Model):
    """
    Description: Model Description
    """
    faculty = models.ForeignKey('Faculty', 
        on_delete=models.CASCADE, 
        related_name="get_learn_table")
    for_class = models.ForeignKey('schoolclasses.SchoolClass',
        on_delete=models.CASCADE,
        related_name="get_learn_table")
    def __str__(self):
        return "%s %s" % (self.faculty,self.for_class)

    def get_url_obj(self):
        return reverse("learn-table",args=[self.id])

    class Meta:
        pass

class Mark(models.Model):
    """
    Description: Model Description
    """
    
    mark_date = models.DateField(auto_now=False, auto_now_add=False)
    
    learn_table = models.ForeignKey(
        'LearnTable',
        on_delete=models.CASCADE,
        related_name='get_marks')
    who_get_mark = models.ForeignKey(
        'schoolclasses.Pupil', 
        related_name="get_marks",
        on_delete=models.CASCADE,
        null=True,
        blank=True
        )

    def save(self, *args, **kwargs):
        
        super(Mark, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.who_get_mark)


    class Meta:
        pass

class Pip(models.Model):
    """
    Description: Model Description
    """
    pips = models.IntegerField()
    mark = models.ForeignKey('Mark', related_name="pips",
        on_delete=models.CASCADE)

    class Meta:
        pass