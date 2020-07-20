from django import forms

class KitabForm(forms.Form):
    kategori = forms.CharField()
    nama_kitab = forms.CharField()
    nama_pengarang = forms.CharField(required=False)
    file_kitab = forms.FileField(required=False)