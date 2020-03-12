from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order # which model to use
        fields = '__all__' # creates form with all fields

