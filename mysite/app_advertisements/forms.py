from django import forms


class AdvertisementForm(forms.Form):
    title = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class': 'form-control-lg'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control-lg'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control-lg'}))
    is_auction = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-control-lg'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-lg'}))
