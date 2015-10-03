from django.conf.urls import url
from .views import page

urlpatterns = [
    # (?!\/+) - fail if sequence starts with a slash
    url(r'^(?P<slug>(?!\/+)[\w/-]+).html$', page, name='page'),
]
