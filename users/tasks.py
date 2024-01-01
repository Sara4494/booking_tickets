from celery import shared_task
from django.core.mail import EmailMessage
from .models import User
import random
@shared_task
def send_email(user_email,user_otp):
    email_message = EmailMessage('MaskneApp', f'Your OTP is {user_otp}, if you got any problem please connect with the support team',to=[user_email])
    email_message.send()
@shared_task
def otp_generating_task():
    number_list = [x for x in range(10)] 
    code_items_for_otp = []
    for i in range(4):
        num = random.choice(number_list)
        code_items_for_otp.append(num)
    code_string = "".join(str(item)for item in code_items_for_otp)
    users = User.objects.all()
    for user in users:
        user.otp = code_string
        user.save()