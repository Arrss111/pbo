from django import forms
from .models import order


class orderform(forms.ModelForm):
    full_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Full Name'}), required=True)
    email = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'email'}), required=True)
    deskripsi = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'deskripsi'}), required=True)
    Nomor_HP = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nomor_HP'}), required=False)



    class Meta:
        model = order
        fields = ['full_name', 'email', 'deskripsi', 'Nomor_HP']

        exclude = ['user', ]
