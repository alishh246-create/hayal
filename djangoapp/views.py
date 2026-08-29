from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from .models import Contact

# Home page
def index(request):
    return render(request, 'index.html')

# Booking page
def booking(request):
    return render(request, 'booking.html')

# Contact page
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            # Email notification to admin
            send_mail(
                subject='New Booking Inquiry — Hayal Events',
                message=f'''Assalam-o-Alaikum,

You have received a new inquiry through the Hayal Events website. Details are as follows:

Name: {contact.name}
Phone: {contact.phone}
Email: {contact.email}
Address: {contact.address}

Message:
{contact.message}

Please respond to the client at your earliest convenience.

Regards,
Hayal Events Website
''',
                from_email='hayalevents123@gmail.com',
                recipient_list=['alishh246@gmail.com'],
                fail_silently=False,
            )

            return redirect('thankyou')
    else:
        form = ContactForm()

    contacts = Contact.objects.all().order_by('-created_at')
    return render(request, 'contact.html', {'form': form, 'contacts': contacts})

# Map view for Contacts
def contacts_map(request):
    contacts = Contact.objects.all().order_by('-created_at')
    return render(request, 'contacts_map.html', {'contacts': contacts})

# Other pages
def diamond(request):
    return render(request, 'diamond.html')

def events(request):
    return render(request, 'events.html')

def gallery(request):
    return render(request, 'gallery.html')

def gold(request):
    return render(request, 'gold.html')

def premium(request):
    return render(request, 'premium.html')

def services(request):
    return render(request, 'services.html')

# Thank you page
def thankyou(request):
    return render(request, 'thankyou.html')