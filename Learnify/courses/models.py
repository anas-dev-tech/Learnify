from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()



class Subject(models.Model):
    title  = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        ordering = ['title']
        
    def __str__(self) -> str:
        return self.title
    
class Course(models.Model):
    owner = models.ForeignKey(
        User,
        related_name='courses_created',
        on_delete=models.CASCADE
    )

    subject = models.ForeignKey(
        Subject,
        related_name= 'courses',
        on_delete=models.CASCADE
    )
    
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']
    

    def __str__(self) -> str:
        return self.title

    
class Module(models.Model):
    course = models.ForeignKey(
        Course,
        related_name='modules',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

