from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import KitabForm
from .models import UploadKitab

def upload(request):
    form_field = KitabForm()

    context = {
        'kitab_form' : form_field,
    }

    if(request.method=="POST"):
        print(request.POST)
        UploadKitab.objects.create(
            username = request.user,
            kategori = request.POST['kategori'],
            nama_kitab = request.POST['nama_kitab'],
            nama_pengarang = request.POST['nama_pengarang'],
            file_kitab = request.POST['file_kitab'],
        )
        return HttpResponseRedirect("/")

    return render(request, 'kitab/index.html', context)