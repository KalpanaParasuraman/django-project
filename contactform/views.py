
# Create your views here.
from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    submitted = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()   #saves to database
            submitted = True
    else:
        form = ContactForm()

    return render(request, 'contactform/contact.html', {'form': form, 'submitted': submitted})