from django.contrib import admin
from .models import Message




@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    '''Admin View for Message'''

    list_display = ('sent_on', 'user', 'course', 'content')
    list_filter = ('sent_on', 'course')
    search_fields = ('content',)
    raw_id_fields = ('user', 'course')
    date_hierarchy = 'sent_on'
    
