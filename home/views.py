from django.shortcuts import render, redirect
from django.contrib.auth.admin import User
from django.contrib import messages
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from services.forms import FreeQuoteForm

# Create your views here.
import os


def homepage(request):
    context = {}
    return render(request, 'home/HomePage.html', context)


def AboutView(request):
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

    context = {"quote_form": quote_form}
    return render(request, "home/AboutPage.html", context)
