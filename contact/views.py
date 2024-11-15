from django.shortcuts import render, redirect
from .models import  Contact
from .forms import ContactForm
from django.http import HttpResponse


# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
        return render(request, 'contact/contact_form.html', {'form': form})


def contact_form(request):
    return render(request, 'contact/contact.html')







