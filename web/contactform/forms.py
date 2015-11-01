from django import forms
from django.core.mail import send_mail
from django.conf import settings
from multiprocessing import Process


class ContactForm(forms.Form):
    name = forms.CharField(label=u"Your name", required=True,
                           widget=forms.TextInput(attrs={"placeholder": u"Your name"}))
    email = forms.EmailField(label=u"Your email",
                             widget=forms.TextInput(attrs={"placeholder": u"Your email"}))
    message = forms.CharField(label=u"Your message",
                              widget=forms.Textarea(attrs={"placeholder": u"Your message"}))

    def send_email(self):
        name = self.cleaned_data["name"]
        email = self.cleaned_data["email"]
        message = self.cleaned_data["message"]

        # Make it async for the sake of responsibility
        p = Process(target=send_mail, kwargs={
            "subject": u"[rootxnet.com] message from: {}".format(name),
            "from_email": email,
            "message": message,
            "recipient_list": settings.EMAIL_RECIPIENTS,
        })
        p.start()
