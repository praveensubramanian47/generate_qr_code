from django import forms


class QRCodeForm(forms.Form):
    restaurant_name = forms.CharField(
        max_length=50, 
        label='Restaurant',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter restaurant name'
        }))
    url = forms.URLField(
        max_length=200, 
        label='Menu URL',
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter menu URL'
        }))