from django.contrib.auth.models import User
from django.views.generic import FormView
from django.shortcuts import redirect
from .forms import RegistrationForm


class RegistrationView(FormView):
    form_class = RegistrationForm
    success_url = 'home'
    model = User
    template_name = 'user/registration.html'

    def form_valid(self, form):
        form_data = form.cleaned_data
        user = User()
        user.username = form_data['username']
        user.email = form_data['email']
        user.set_password(form_data['password'])
        user.save()
        return redirect(self.success_url)
