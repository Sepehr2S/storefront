from django.core.mail import BadHeaderError, mail_admins, send_mail
from django.shortcuts import render

def say_hello(request):
    try:
        send_mail('subject', 'message', 'info@sep.com', ['jesus@sep.com','namosan@sep.com'])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Sepehr'})
