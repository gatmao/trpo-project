from django.views.generic import TemplateView


class CreateDealView(TemplateView):
    template_name = 'deal/create.html'
