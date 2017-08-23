from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

class EmailMixin(object):

    def __init__(self, *args, **kwargs):
        return super(EmailMixin, self).__init__(*args, **kwargs)

    def _send_email(self, data):
        subject = data.get('subject')
        from_email = settings.EMAIL_HOST_USER
        to = data.get('email_to')
        html_content = data.get('template')

        msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
        msg.content_subtype = "html"
        msg.send()

    def user_invite(self, email, url):

        data = {
            "email_to": email,
            "subject" : "Invitation on SwiftTracker",
            "template": render_to_string('email/user_invitation.html',{
                'signup_link': url,
                'admin': self.request.user.get_full_name()
            })
        }

        self._send_email(data) 