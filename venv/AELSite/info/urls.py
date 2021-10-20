from django.urls import path, include
from .views import landing, contact, courses, about

urlpatterns = [
    path('', landing, name='landing'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('courses/', courses, name='courses'),
    path('faq/', include('faq.urls'), name='faq')
]