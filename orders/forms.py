# создадим форму, данные из которой будут передаваться в модель Subscribes
from django import forms


# данная форма не привязана к модели
class CheckoutContactForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
