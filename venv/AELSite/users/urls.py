from django.urls import path, include
from .views import logout_view

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('accounts/', include('django.contrib.auth.urls'))
]