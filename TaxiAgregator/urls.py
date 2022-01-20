import TaxiAgregator.views
from . import views
from django.urls import path, include
from django.contrib.auth import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', TaxiAgregator.views.signup),
    path('order/', TaxiAgregator.views.order),
    path('check_order/', TaxiAgregator.views.check_order),
    path('history/', TaxiAgregator.views.history),
    path('logout/', views.LogoutView.as_view())
]