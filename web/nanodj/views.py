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
    """
    Safely lookup a ``file_name`` in ``settings.PAGE_BUILD_DIR``, render it using Django templating system,
    pull the metadata and return a dictionary containing all the relevant information about the file.

    :parameter file_name:   Name of a file to be pulled from ``settings.PAGE_BUILD_DIR`` directory.
    :returns:   ``Dict`` object containing:
        * ``title`` - file name
        * ``html`` - contents of a pulled file
        * ``metadata`` - metadata extracted from source .ipynb file
        * ``url`` - a permalink to the file in question
    """
    name, ext = os.path.splitext(file_name)

    try:
        file_path = safe_join(settings.PAGE_BUILD_DIR, file_name)
    except SuspiciousFileOperation:
        raise Http404('Page Not Found')
    else:
        if not os.path.exists(file_path):
            raise Http404('Page Not Found')

    with open(file_path, 'r') as f:
        html_content = Template(f.read())

        meta_file = safe_join(settings.PAGE_BUILD_DIR, "{}.METADATA".format(name))
        metadata = None
        if os.path.isfile(meta_file):
            with open(meta_file) as meta:
                try:
                    metadata = json.loads(meta.read())
                except ValueError:
                    pass
    return {
        "title": name,
        "html": html_content,
        "metadata": metadata,
        "url": reverse(page, kwargs={"slug": name}),
    }


def page(request, slug):
    return render(
        request,
        "ipynb_page.html",
        context={
            "page": get_page_or_404("{}.html".format(slug)),
        }
    )
