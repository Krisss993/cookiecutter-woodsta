from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f"Zapytanie od: {form.cleaned_data['name']}",
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['woodsta2025@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Wiadomość została wysłana pomyślnie!')
            return redirect('contact_form')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})