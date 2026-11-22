from django.urls import path
from .views import RegistarView, LoginView, LogoutView

urlpatterns = [
    path('reg/', RegistarView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
