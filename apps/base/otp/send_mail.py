from django.core.mail import send_mail
from django.template.loader import render_to_string

def send_otp_email(user, otp):
    try:
        # Load the HTML template
        html_message = render_to_string('emails/otp_email_template.html', {
            'username': user.username,
            'otp': otp,
        })
        
        # Load the plain text template
        plain_message = render_to_string('emails/otp_email_template.txt', {
            'username': user.username,
            'otp': otp,
        })

         # Include OTP in the subject line
        subject = f'Your OTP Code {otp} - Quick Verification'

        send_mail(
            subject,
            plain_message,
            'usernamezxc0@gmail.com',
            [user.email],
            fail_silently=False,
            html_message=html_message, 
        )
    except Exception as e:
        raise Exception(f"Error sending email: {str(e)}")
