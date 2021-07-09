from django.contrib import messages
from django.shortcuts import render
from services.forms import FreeQuoteForm
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Create your views here.


def Service_view(request):
    context = {}
    if request.method == "POST":
        quote_form = FreeQuoteForm(request.POST)
        if quote_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            sendgrid_message = Mail(
                from_email=email,
                to_emails="overbergsoftware@Gmail.com",
                subject="webapp_coder.com Free Quote",
                html_content="NAME: " + name + "<br>MESSAGE: " + message
            )

            try:
                sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                response = sg.send(sendgrid_message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
                messages.success(request, "Thank you, we'll get back to you as soon as possible")

            except Exception as e:
                print(e)
    else:
        quote_form = FreeQuoteForm()
        context["quote_form"] = quote_form

    return render(request, "services/ServicesPage.html", context)
