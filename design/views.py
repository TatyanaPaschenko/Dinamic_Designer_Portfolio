from django.http import HttpResponse
from django.views.generic import DetailView
from django.views.generic import ListView

from portfolio.settings import STATIC_PATH
import os

from design.models import PhotoModel, InfoInMainPage
from contactme.forms import ContactForm


class ContextInfoMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = PhotoModel.objects.all()
        context['main_info'] = InfoInMainPage.objects.all()
        context['form'] = ContactForm
        return context


class MainPageView(ContextInfoMixin, ListView):
    template_name = 'design/index.html'
    model = PhotoModel


class ProjectDetailView(ContextInfoMixin, DetailView):
    template_name = 'design/detail.html'
    model = PhotoModel


def download(request):
    path = os.path.join(STATIC_PATH, 'files', 'cv.pdf')
    file = open(path, 'rb')
    body = file.read()
    response = HttpResponse(body, content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename=cv.pdf'
    return response
