from django.core.urlresolvers import reverse_lazy, reverse
from django.utils.functional import lazy
from .forms import ContactForm
from django.views.generic.edit import FormView


class ContactView(FormView):
    template_name = 'contactform/contact_page.html'
    form_class = ContactForm

    def get_success_url(self):
        return "{}?message_sent=true".format(reverse("contact"))

    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context["message_sent"] = self.request.GET.get("message_sent", False)
        return context
