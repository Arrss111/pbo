from django import forms
from .models import order, karyaSeni


class orderform(forms.ModelForm):
    full_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Full Name'}), required=True)
    email = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'email'}), required=True)
    deskripsi = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'deskripsi'}), required=True)
    Nomor_HP = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nomor_HP'}), required=True)
    product = forms.ModelChoiceField(label="", queryset=karyaSeni.objects.all(), widget=forms.Select(attrs={'class':'form-control', 'placeholder':'Karya_seni'}), required=True)



    class Meta:
        model = order
        fields = ['full_name', 'email', 'deskripsi', 'Nomor_HP', "product"]

        exclude = ['user', ]
