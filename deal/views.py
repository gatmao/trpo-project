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
        if deal_type == 'sell':
            buyer, seller = participant, me
        elif deal_type == 'buy':
            buyer, seller = me, participant
        else:
            raise ValueError("unknown deal type")
        deal = Deal(deal_name=form.data['deal_name'],
                    deal_state='pending',
                    description=form.data['description'],
                    buyer=buyer,
                    seller=seller,
                    price=form.data['price'])
        deal.save()
        return super(CreateDealView, self).form_valid(form)


class ListDealView(ListView):
    model = Deal

    def get_queryset(self):
        me = self.request.user
        return Deal.objects.filter(Q(buyer=me) | Q(seller=me))
