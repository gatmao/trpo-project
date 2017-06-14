from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegistrationView

urlpatterns = [
    url(r'login$', LoginView.as_view(template_name='user/login.html'), name='login'),
    url(r'logout$', LogoutView.as_view(next_page='home'), name='logout'),
    url(r'registration$', RegistrationView.as_view(), name='registration')
]