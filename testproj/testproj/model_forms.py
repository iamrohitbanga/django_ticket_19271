from django.forms import ModelForm
from django import forms
from models import *

class BaseModelForm(ModelForm):
    class Meta:
        model = BaseModel
        exclude = ('group') 

class BaseGroupForm(ModelForm):
    class Meta:
        model = BaseGroup

