from django.urls import path
from form_app.views import *

urlpatterns = [
    path('', register_view, name= 'register_view'),
    path('login/', login_view, name= 'login_view'),
    
]