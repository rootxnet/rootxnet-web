from django.conf.urls import include, url
from django.views.generic import TemplateView, RedirectView
import nanodj.urls

urlpatterns = [
    url(r'^blog/$', TemplateView.as_view(template_name='blog.html'), name='blog'),
    url(r'^blog/', include(nanodj.urls), ),
    url(r'^Michal-Lech-Resume.pdf$',
        RedirectView.as_view(
            url="https://www.dropbox.com/s/grkahe90fkbkv1n/Michal-Lech-Resume.pdf?dl=0",
            permanent=False
        ),
        name='download_resume'
    ),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
]
