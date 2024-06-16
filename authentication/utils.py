import random
from django.core.mail import send_mail
from django.conf import settings


def otp_email_verification(user):
    otp = str(random.randint(100000, 999999))
    print(otp)
    user.otp = otp
    user.save()
    return otp


def send_verification_email(user, pin):
    subject = 'K-Pentag OTP Verification'
    message = f'Your OTP is: {pin}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)