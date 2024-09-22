from django.db import models
from django.contrib.auth import get_user_model
from .subject import Subject

User = get_user_model()

class Course(models.Model):
    owner = models.ForeignKey(
        User,
        related_name='courses_created',
        on_delete=models.CASCADE
    )
    students = models.ManyToManyField(
        User,
        related_name='courses_joined',
        blank=True
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
