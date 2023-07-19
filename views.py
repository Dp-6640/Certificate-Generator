from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import hashlib
from reportlab.pdfgen import canvas
from io import BytesIO
import random
import string
import jwt
from datetime import datetime, timedelta

from .models import Certificate, VerificationToken

def generate_certificate_pdf(title, content):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 800, title)
    p.drawString(100, 750, content)
    p.save()
    buffer.seek(0)
    return buffer

@login_required
def generate_certificate(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        if title and content:
            certificate = Certificate.objects.create(
                title=title,
                content=content,
                user=request.user
            )
            certificate.save()

            pdf_buffer = generate_certificate_pdf(title, content)
            response = HttpResponse(pdf_buffer, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{title}.pdf"'
            return response

    return render(request, 'generate_certificate.html')

def generate_certificate_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def hash_certificate_code(code):
    return hashlib.sha256(code.encode()).hexdigest()

def create_verification_token(certificate):
    code = generate_certificate_code()
    hashed_code = hash_certificate_code(code)

    token = VerificationToken.objects.create(
        certificate=certificate,
        token=hashed_code
    )
    token.save()

    return code

def verify_certificate(request):
    if request.method == 'POST':
        certificate_code = request.POST.get('certificate_code')
        if certificate_code:
            hashed_code = hash_certificate_code(certificate_code)
            try:
                token = VerificationToken.objects.get(token=hashed_code)
                certificate = token.certificate
                return render(request, 'certificate_verification_result.html', {'certificate': certificate})
            except ObjectDoesNotExist:
                return render(request, 'certificate_verification_result.html', {'error': 'Certificate not found'})

    return render(request, 'certificate_verification.html')

def customize_certificate(request, certificate_id):
    try:
        certificate = Certificate.objects.get(id=certificate_id, user=request.user)
    except ObjectDoesNotExist:
        return redirect('home')  # You should replace 'home' with the appropriate URL name for your homepage.

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        if title and content:
            certificate.title = title
            certificate.content = content
            certificate.save()

    return render(request, 'customize_certificate.html', {'certificate': certificate})

@login_required
def home(request):
    return render(request, 'home.html')
