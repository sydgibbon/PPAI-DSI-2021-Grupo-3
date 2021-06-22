from django import forms

class TarifaForm(forms.Form):
    tarifa = forms.IntegerField(max_value=999, required=True)
    
class CtdadEntradasForm(forms.Form):
    ctdadEntradas = forms.IntegerField(max_value=999, required=True)