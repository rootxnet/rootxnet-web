import os
import sys
from django.conf import settings
from django.core.wsgi import get_wsgi_application

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
settings.configure(
    DEBUG=True,
    ROOT_URLCONF='urls',
    MIDDLEWARE_CLASSES=(),
    INSTALLED_APPS=(
        # 'django.contrib.staticfiles',
        # 'django.contrib.webdesign',
        'nanodj',
    ),
    STATIC_URL='/static/',
    TEMPLATE_DIRS=["templates", ],
    TEMPLATE_CONTEXT_PROCESSORS=["nanodj.context_processors.all_ipynb_pages", ],
    PAGE_SOURCE_DIR=os.path.join(BASE_PATH, "source"),
    PAGE_BUILD_DIR=os.path.join(BASE_PATH, "build"),
)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
else:
    application = get_wsgi_application()
