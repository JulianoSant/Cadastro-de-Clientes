from django.forms import ModelForm
from app.models import Cliente

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'idade', 'cod']
