from django.shortcuts import render , redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def mail(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject,message,email_from,recipient_list)
        request.session['msg'] = "Message has been sent."
        return redirect('success')
    messages.success(request, "Welcome To Mail.")
    return render(request , 'mail.html')


def success(request):
    messages.success(request,request.session['msg'])
    return render(request,'success.html')
    