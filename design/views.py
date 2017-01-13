from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView

from design.models import PhotoModel


class MainPageView(ListView):
    template_name = 'design/index.html'
    model = PhotoModel

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     file_id = self.request.GET.get('course_id', None)
    #     if course_id:
    #         qs = qs.filter(courses__id=course_id)
    #     return qs

class ProjectDetailView(DetailView):
    template_name = 'design/detail.html'
    model = PhotoModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['/'] = '/'
        return context


class LinkView(TemplateView):
    template_name = 'design/test.html'
    model = PhotoModel



