from django.views.generic import FormView
from django.shortcuts import redirect
from .forms import RegistrationForm, PaymentForm
from photo_trade.settings import AUTH_USER_MODEL


class RegistrationView(FormView):
    form_class = RegistrationForm
    success_url = 'home'
    template_name = 'user/registration.html'

    def form_valid(self, form):
        form_data = form.cleaned_data
        user = AUTH_USER_MODEL()
        user.username = form_data['username']
        user.email = form_data['email']
        user.set_password(form_data['password'])
        user.save()
        return redirect(self.success_url)


class PaymentView(FormView):
    form_class = PaymentForm
    success_url = 'home'
    template_name = 'user/pay.html'
    current_user = None

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            self.current_user = request.user
        return super(PaymentView, self).post(request, args, kwargs)

    def form_valid(self, form):
        payment = form.cleaned_data['payment']
        if self.current_user:
            self.current_user.ballance += payment
            self.current_user.save()
        return redirect(self.success_url)
