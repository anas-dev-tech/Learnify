from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()





class Message(models.Model):
    '''Model definition for Message.'''
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='chat_messages'
    )
    course = models.ForeignKey(
        'courses.Course',
        on_delete=models.CASCADE,
        related_name='chat_message'
    )
    content = models.TextField()
    sent_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user} on {self.course} at {self.sent_on}'
    
    
    

    class Meta:
        '''Meta definition for Message.'''

        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        pass
