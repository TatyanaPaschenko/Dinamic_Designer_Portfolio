from django.conf.urls import url
from . import views

app_name = 'design'
urlpatterns = [
    url(r'^$', views.MainPageView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.ProjectDetailView.as_view(), name='detail'),
    url(r'^test/$', views.LinkView.as_view(), name ='test')
]
