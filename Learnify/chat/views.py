from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from courses.models import Course
from django.http import HttpResponseForbidden

@login_required
def course_chat_room(request, course_id):
    try:
        course = request.user.courses_joined.get(id=course_id)
    except Course.DoesNotExist:
        return HttpResponseForbidden()
    latest_messages = course.chat_message.select_related(
        'user'
    ).order_by('-sent_on')[:10]
    
    return render(
        request,
        'chat/room.html',
        {
            'course':course,
            'latest_messages':latest_messages,
        }
    )
        



