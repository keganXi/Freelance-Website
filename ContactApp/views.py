from django.shortcuts import render, redirect
from django.contrib import messages
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from ContactApp.forms import ContactForm
from ContactApp.models import ClientContactDatabase

# Create your views here.


def Contact_us_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            full_name = request.POST.get('full_name')
            company_name = request.POST.get('company_name')
            email = request.POST.get('email')
            referrel = request.POST.get('referrel')
            message = request.POST.get('message')
            email_enquiry(email, full_name, message, request, company_name, referrel)

    else:
        form = ContactForm()

    context = {
        'form': form
    }
    return render(request, 'ContactApp/ContactUsPage.html', context)


# CONTACT EMAIL FUNCTION.
def email_enquiry(email, full_name, message, request, company_name="none", referrel="none"):
    sendgrid_message = Mail(
        from_email=email,
        to_emails="overbergsoftware@Gmail.com",
        subject="webapp_coder.com Contact Enquirer",
        html_content="<Strong>NAME:</Strong> " + full_name + "<br><br><Strong>MESSAGE:</Strong> " + message
                     + "<br><br><Strong>Where did you hear about us:</Strong> " +
                     str(referrel) + "<br><br><Strong>Company name:</Strong> " + str(company_name)
    )

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(sendgrid_message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        messages.success(request, "Thank you, we'll get back to you as soon as possible")

        # SAVE USER INFORMATION TO ACCOUNT DATABASE.
        account_db = ClientContactDatabase(
            full_name=full_name, company_name=company_name, email=email,
            referrel=referrel, message=message
        )
        account_db.save()

    except Exception as e:
        print(e)
