from socket import fromshare
from django import forms
from ..models import billModel
from django.db import models
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, ButtonHolder, Submit

class BillForm(forms.ModelForm):
    
    class Meta:
        model=billModel

        fields=[
            "cname",
            "product",
            "price",
            "status",
        ]