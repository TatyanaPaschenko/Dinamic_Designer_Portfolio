from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView

from portfolio import settings
from portfolio.settings import STATIC_PATH
import os

from design.models import PhotoModel, Feedback
from design.forms import ContactForm


class MainPageView(CreateView):
    template_name = 'design/index.html'
    model = Feedback
    success_url = reverse_lazy('design:index')
    form_class = ContactForm

    def form_valid(self, form):
        s = super().form_valid(form)
        messages.success(self.request, "Thank you for your message! I will keep in touch with you very soon!")
        send_mail(self.object.subject, self.object.message, self.object.from_email, settings.ADMINS)
        return s

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = PhotoModel.objects.all()
        return context

# class IncludeContactFormView(CreateView):
#     template_name = '/contact_me.html'
#     model = Feedback
#     success_url = reverse_lazy('design:index')
#     form_class = ContactForm
#
#     def form_valid(self, form):
#         s = super().form_valid(form)
#         messages.success(self.request, "Thank you for your feedback! We will keep in touch with you very soon!")
#         send_mail(self.object.subject, self.object.message, self.object.from_email, settings.ADMINS)
#         return s


class ProjectDetailView(DetailView):
    template_name = 'design/detail.html'
    model = PhotoModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = PhotoModel.objects.all()
        return context


def download(request):
    path = os.path.join(STATIC_PATH, 'files', 'cv.pdf')
    file = open(path, 'rb')
    body = file.read()
    response = HttpResponse(body, content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename=cv.pdf'
    return response
