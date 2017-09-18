from django import forms

from user.models import CustomUser


class CreateDealForm(forms.Form):
    deal_name = forms.CharField()
    deal_type = forms.ChoiceField(widget=forms.RadioSelect, choices=(('sell', 'Продать',), ('buy', 'Купить',)))
    description = forms.CharField(max_length=200)
    price = forms.FloatField()
    participant = forms.CharField()

    def clean_participant(self):
        participant = self.cleaned_data['participant']
        if not CustomUser.objects.filter(username=participant).exists():
            raise forms.ValidationError("Нет такого пользователя")
        return participant

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError("Цена должна быть неотрицательной")
        return price
