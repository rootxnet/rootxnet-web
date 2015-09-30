from django.conf.urls import include, url
from django.views.generic import TemplateView
import nanodj.urls

urlpatterns = [
    url(r'^blog/', include(nanodj.urls),),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
]