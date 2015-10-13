import os
import json
from django.shortcuts import render
from django.conf import settings
from django.http import Http404
from django.template import Template
from django.utils._os import safe_join
from django.core.urlresolvers import reverse
from django.core.exceptions import SuspiciousFileOperation


def get_page_or_404(file_name):
    """Return page content as a Django template or raise 404 error."""
    try:
        file_path = safe_join(settings.PAGE_BUILD_DIR, "{}.html".format(file_name))
    except SuspiciousFileOperation:
        raise Http404('Page Not Found')
    else:
        if not os.path.exists(file_path):
            raise Http404('Page Not Found')

    with open(file_path, 'r') as f:
        html_content = Template(f.read())

        meta_file = safe_join(settings.PAGE_BUILD_DIR, "{}.METADATA".format(file_name))
        metadata = None
        if os.path.isfile(meta_file):
            with open(meta_file) as meta:
                try:
                    metadata = json.loads(meta.read())
                except ValueError:
                    pass

    return {
        "title": file_name,
        "html": html_content,
        "metadata": metadata,
        "url": reverse(page, kwargs={"slug": file_name}),
    }


def page(request, slug):
    return render(
        request,
        "ipynb_page.html",
        context={
            "page": get_page_or_404(slug),
        }
    )
