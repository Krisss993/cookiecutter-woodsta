from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from forms.forms import ContactForm
from django.http import HttpResponse, HttpResponseServerError
import logging


logger = logging.getLogger(__name__)


# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             send_mail(
#                 subject=f"Zapytanie od: {form.cleaned_data['name']}",
#                 message=form.cleaned_data['message'],
#                 from_email=form.cleaned_data['email'],
#                 recipient_list=['woodsta2025@gmail.com'],
#                 fail_silently=False,
#             )
#             messages.success(request, 'Wiadomość została wysłana pomyślnie!')
#             return redirect('contact_form')
#     else:
#         form = ContactForm()
#     return render(request, 'home.html', {'form': form})


# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             send_mail(
#                 subject=f"Zapytanie od: {form.cleaned_data['name']}",
#                 message=form.cleaned_data['message'],
#                 from_email=form.cleaned_data['email'],
#                 recipient_list=['woodsta2025@gmail.com'],
#                 fail_silently=False,
#             )
#             messages.success(request, 'Wiadomość została wysłana pomyślnie!')
#             return redirect('home')
#     else:
#         form = ContactForm()
#     return render(request, 'home.html', {'form': form})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Wiadomość z formularza kontaktowego"
            body = f"{form.cleaned_data['name']} <{form.cleaned_data['email']}>:\n\n{form.cleaned_data['message']}"
            try:
                send_mail(subject, body, 'noreply@woodsta.onrender.com', ['yourcompany@example.com'])
                return redirect('home')
            except Exception as e:
                logger.error("Error sending email: %s", e)
                return HttpResponseServerError("Internal server error")
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})





# def send_email_view(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

#         full_message = f"Od: {name} <{email}>\n\n{message}"

#         send_mail(
#             subject=subject,
#             message=full_message,
#             from_email=settings.DEFAULT_FROM_EMAIL,
#             recipient_list=['woodsta2025@gmail.com'],
#         )
#         messages.success(request, "Wiadomość została wysłana. Dziękujemy za kontakt!")
#         return redirect('home')
#     else:
#         return redirect('home')
