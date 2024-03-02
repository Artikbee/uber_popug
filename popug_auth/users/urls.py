from django.urls import path

from . import views

urlpatterns = [
    path('me', views.CustomMeView.as_view(
        actions={'get': 'me', 'put': 'me', 'delete': 'me'})),
    path('registration', views.RegistrationView.as_view(), name='user-reg'),
]
