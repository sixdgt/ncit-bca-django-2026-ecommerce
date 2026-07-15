# for helper functions related to accounts app
# for instance: verification code generation, email sending and so on
import random
import string
from django.core.mail import send_mail
from django.conf import settings

def generate_verification_code():
    """
    This function will generate a random 6 digit verification code for user verification.
    """
    code = ''.join(random.choices(string.digits, k=6))
    # it will generate a random 6 digit code using digits from 0-9
    return code

def send_verification_email(user_email, verification_code):
    """
    This function will send a verification email to the user with the provided verification code.
    """
    subject = 'My E-Commerce App Email Verification'
    message = f"Your account verification code is: {verification_code}"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    send_mail(subject, message, from_email, recipient_list)