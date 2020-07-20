from django import forms

class ReviewForm(forms.Form):
    review = forms.CharField()

    CHOICE = [('Iya', 'Iya'), ('Tidak', 'Tidak')]
    relevan = forms.ChoiceField(choices=CHOICE, label='Apakah dokumen dari hasil pencarian relevan?')