from django import forms

class KitabForm(forms.Form):
    kategori = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
                                                                'class': 'form-control item',
                                                                }))
    nama_kitab = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
                                                                'class': 'form-control item',
                                                                }))
    nama_pengarang = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={
                                                                'class': 'form-control item',
                                                                }))
    file_kitab = forms.FileField(widget=forms.ClearableFileInput())