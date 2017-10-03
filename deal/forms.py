import os
from django import forms

from user.models import CustomUser


class CreateDealForm(forms.Form):
    deal_name = forms.CharField()
    deal_type = forms.ChoiceField(widget=forms.RadioSelect, choices=(('sell', 'Продать',), ('buy', 'Купить',)))
    description = forms.CharField(max_length=200)
    price = forms.FloatField()
    participant = forms.CharField()
    image = forms.FileField()

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

    def clean_image(self):
        image = self.cleaned_data['image']
        ext = os.path.splitext(image.name)[1]
        valid_extensions = ['.png', '.jpeg']
        if not ext.lower() in valid_extensions:
            raise forms.ValidationError("Файл должен быть картинкой")
        return image
