from django import forms
from .models import *
  
class HotelForm(forms.ModelForm):
  
    class Meta:
        model = Images
        fields = ['name', 'images_Main_Img']