from django.shortcuts import render
from .models import Logo


def home(request):
    """ A View to return the HOME page """

    logos = Logo.objects.all()

    context = {
        'logos': logos,
    }

    return render(request, 'home.html', context)


def contact(request):
    """ A view to return CONTACT page """

    return render(request, 'contact.html')
