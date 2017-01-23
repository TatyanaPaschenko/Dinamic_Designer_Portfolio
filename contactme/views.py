from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from contactme.forms import ContactForm

from contactme.models import Feedback
from portfolio import settings


class ContactView(CreateView):
    template_name = 'include/contact_form_include.html'
    model = Feedback
    success_url = reverse_lazy('design:index')
    form_class = ContactForm

    def form_valid(self, form):
        s = super().form_valid(form)
        messages.success(self.request, "Thank you for your message! I will keep in touch with you very soon!")
        send_mail(self.object.name, self.object.message, self.object.email, settings.ADMINS)
        return s
