from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            email_message = EmailMessage(
                'New Contact Form Submission',
                f'Name: {name}\nPhone Number: {phone_number}\nEmail: {email}\nMessage: {message}',
                'abdulrazzaqchohan1@gmail.com',
                ['abdulrazzaqchohan1@gmail.com'],
                reply_to=[email]
            )
            email_message.send()
            return render(request, 'contact.html', {'form': form, 'success': True})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
