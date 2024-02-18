from django.urls import path
from .views import resume_page


app_name = 'resume'

urlpatterns = [
    path('', resume_page, name='resume')
]