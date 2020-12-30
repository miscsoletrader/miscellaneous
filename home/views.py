from django.shortcuts import render


def home(request):
    """ A View to return the HOME page"""

    return render(request, 'home.html')
