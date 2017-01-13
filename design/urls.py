from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'design'
urlpatterns = [
    url(r'^$', views.MainPageView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.ProjectDetailView.as_view(), name='detail'),
    url(r'^test/$', views.LinkView.as_view(), name ='test')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
