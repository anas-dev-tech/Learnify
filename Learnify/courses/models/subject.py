from django.db import models

class Subject(models.Model):
    title  = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        ordering = ['title']
        
    def __str__(self) -> str:
        return self.title
    
    