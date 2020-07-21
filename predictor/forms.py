from django import forms

class ReviewForm(forms.Form):
    query = forms.CharField(max_length=100)
    review = forms.CharField(max_length=500)

    CHOICE = [('Iya', 'Iya'), ('Tidak', 'Tidak')]
    relevan = forms.ChoiceField(choices=CHOICE, label='Apakah dokumen dari hasil pencarian relevan?')