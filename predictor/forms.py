from django import forms

class ReviewForm(forms.Form):
    Query = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
                                                                'class': 'form-control item',
                                                                }))
    review = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
                                                                'class': 'form-control item',
                                                                }))
    # CHOICE = [('Iya', 'Iya'), ('Tidak', 'Tidak')]
    # ANGKA = [(x, str(x)) for x in range(0, 11)]
    ANGKA = ((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'))
    # ANGKA = range(0, 11, 1)
    relevan = forms.ChoiceField(choices=ANGKA, label='Berapa jumlah dokumen yang relevan dari hasil pencarian dokumen?')