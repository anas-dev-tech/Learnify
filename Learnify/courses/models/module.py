from django.db import models
from .course import Course
from courses.fields import OrderField


class Module(models.Model):
    course = models.ForeignKey(
        Course,
        related_name='modules',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['course']) 

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.title}. {self.order}'
    

