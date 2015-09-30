import os
from django.core.urlresolvers import reverse
from django.conf import settings
from .views import page


def all_ipynb_pages(request):
    pages = []
    for file_name, ext in map(os.path.splitext, os.listdir(settings.PAGE_BUILD_DIR)):
        pages.append({
            "title": file_name,
            "url": reverse(page, kwargs={"slug": file_name}),
        })
    return {
        "all_ipynb_pages": pages,
    }
