import json
import os
from django.core.urlresolvers import reverse
from django.conf import settings
from .views import page


def all_ipynb_pages(request):
    pages = []
    for file_name, ext in map(os.path.splitext, os.listdir(settings.PAGE_BUILD_DIR)):
        if ext == ".html":
            meta_file = os.path.join(settings.PAGE_BUILD_DIR, "{}.METADATA".format(file_name))
            metadata = None
            if os.path.isfile(meta_file):
                with open(meta_file) as meta:
                    try:
                        metadata = json.loads(meta.read())
                    except ValueError:
                        pass

            pages.append({
                "title": file_name,
                "url": reverse(page, kwargs={"slug": file_name}),
                "metadata": metadata,
            })
    return {
        "all_ipynb_pages": pages,
    }