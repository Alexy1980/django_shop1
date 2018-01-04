# создадим форму, данные из которой будут передаваться в модель Subscribes
from django import forms
from .models import *

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        # необходимо включить
        fields = ["email", "name"]
        # необходимо исключить
        # exclude = ["email", "name"]
