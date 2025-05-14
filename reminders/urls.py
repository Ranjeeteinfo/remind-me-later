from django.urls import path
from .views import ReminderCreateView , index

urlpatterns = [
    path('api/reminders/create/', ReminderCreateView.as_view(), name='create-reminder'),
    path('',index ,name='index')
]
