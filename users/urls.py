from django.urls import path
from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView

app_name = 'users'
urlpatterns = [
	path('users/', RegistrationAPIView.as_view()),
	path('users/login', LoginAPIView.as_view()),
	path('user', UserRetrieveUpdateAPIView.as_view()),
]