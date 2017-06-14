from django.conf.urls import url
from django.views.generic import TemplateView
from .views import CreateDealView

urlpatterns = [
    url(r'create$', CreateDealView.as_view(), name='create'),
    url(r'type$', TemplateView.as_view(template_name='deal/type.html'), name='type')
]