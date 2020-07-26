from django import forms

class ReviewForm(forms.Form):
    Query = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
                                                                'class': 'form-control item',
                                                                }))
    review = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
                                                                'class': 'form-control item',
                                                                }))
    CHOICE = [('Iya', 'Iya'), ('Tidak', 'Tidak')]
    relevan = forms.ChoiceField(choices=CHOICE, label='Apakah dokumen dari hasil pencarian relevan?')