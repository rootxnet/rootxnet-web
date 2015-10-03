import os
from django.shortcuts import render
from django.conf import settings
from django.http import Http404
from django.template import Template
from django.utils._os import safe_join
from django.core.exceptions import SuspiciousFileOperation


def get_page_or_404(name):
    """Return page content as a Django template or raise 404 error."""
    try:
        file_path = safe_join(settings.PAGE_BUILD_DIR, name)
    except SuspiciousFileOperation:
        raise Http404('Page Not Found')
    else:
        if not os.path.exists(file_path):
            raise Http404('Page Not Found')

    with open(file_path, 'r') as f:
        page = Template(f.read())
    return page


def page(request, slug):
    file_name = "{}.html".format(slug)
    page = get_page_or_404(file_name)

    context = {
        "slug": slug,
        "page": page,
    }
    return render(request, "ipynb_page.html", context)
