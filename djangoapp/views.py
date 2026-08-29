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