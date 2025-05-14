from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Imię")
    email = forms.EmailField(required=True, label="Adres e-mail")
    message = forms.CharField(widget=forms.Textarea, required=True, label="Wiadomość")
    phone = forms.CharField(
        label='Numer telefonu (opcjonalnie)',
        max_length=20,
        required=False,  # <-- opcjonalne pole
    )
