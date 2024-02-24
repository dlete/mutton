# imports Django
from django.shortcuts import render

def about(request):
    context = {'bodymessage': "About this project"}
    return render(request, 'core/about.html', context)
