from django.urls import path
from users.views import SignupPageView


urlpatterns = [
    path('', SignupPageView.as_view(), name='signup'),
]