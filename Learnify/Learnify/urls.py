from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from courses.views import CourseListView

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('accounts/', include('allauth.urls')),  # Allauth URLS
    path('course/', include('courses.urls')),
    path('student/', include('students.urls')),
    path('chat/', include('chat.urls', namespace='chat')),
    path('api/', include('courses.api.urls', namespace='api')),
    path('', CourseListView.as_view(), name='course_list'),
    path('__debug__/', include('debug_toolbar.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    