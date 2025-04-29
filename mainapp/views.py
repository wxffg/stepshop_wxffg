from django.shortcuts import render

def index(request):
    title = 'Главная'

    context = {
        'title': title,
    }
    return render(request, 'index.html', context)

def contacts(request):
    return render(request, 'contacts.html')
