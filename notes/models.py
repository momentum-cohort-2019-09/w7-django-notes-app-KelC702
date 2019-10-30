from django.db import models
from django.urls import reverse


# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
         
    
    def item_count(self):
        return self.items.count()    



class NotesItem(models.Model):

    class Meta:
        ordering = ['order']

    body = models.CharField(max_length=255)
    checklist = models.ForeignKey(to=Notes,
                                  on_delete=models.CASCADE,
                                  related_name='items')
    order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body
