from django.http import HttpResponse
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from portfolio import settings
from portfolio.settings import STATIC_PATH
import os

from design.models import PhotoModel



class MainPageView(ListView):
    template_name = 'design/index.html'
    model = PhotoModel


class ProjectDetailView(DetailView):
    template_name = 'design/detail.html'
    model = PhotoModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = PhotoModel.objects.all()
        return context


class LinkView(TemplateView):
    template_name = 'design/test.html'
    model = PhotoModel


def download(request):
    path = os.path.join(STATIC_PATH, 'files', 'cv.pdf')
    file = open(path, 'rb')
    body = file.read()
    response = HttpResponse(body, content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename=cv.pdf'
    return response
