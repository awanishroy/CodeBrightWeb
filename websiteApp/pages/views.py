from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib import messages

def index(request):

    data = {
        'Seo' : ''
    }
    return render(request, 'websiteApp/index.html', data)