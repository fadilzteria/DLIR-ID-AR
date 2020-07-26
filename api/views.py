from django.shortcuts import render

def index(request):
    context = {
        'title': "Kitab Ulama",
    }
    return render(request, 'index.html', context)