from django.db.models import Q
from django.views.generic import ListView, FormView

from deal.forms import CreateDealForm
from deal.models import Deal
from user.models import CustomUser


class CreateDealView(FormView):
    template_name = 'deal/create.html'
    form_class = CreateDealForm
    success_url = '/deal/list/'

    def form_valid(self, form):
        deal_type = form.data['deal_type']
        me = self.request.user
        participant = CustomUser.objects.get(username=form.data['participant'])
        deal = Deal(deal_name=form.data['deal_name'],
                    description=form.data['description'],
                    creator=me,
                    type=form.data['deal_type'],
                    participant=participant,
                    price=form.data['price'],
                    image=self.request.FILES['image'])
        deal.save()
        return super(CreateDealView, self).form_valid(form)


class ListDealView(ListView):
    model = Deal

    def get_queryset(self):
        me = self.request.user
        return Deal.objects.filter(Q(creator=me) | Q(participant=me))

    def get_context_data(self, **kwargs):
        context = super(ListDealView, self).get_context_data(**kwargs)
        context['me'] = self.request.user
        return context
