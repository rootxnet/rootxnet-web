import os
import sys
from django.conf import settings
from django.core.wsgi import get_wsgi_application

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
NANO_DEBUG = os.environ.get("NANO_DEBUG", False)
settings.configure(
    BASE_PATH=BASE_PATH,
    DEBUG=NANO_DEBUG,
    ALLOWED_HOSTS=["*", ],
    ROOT_URLCONF='urls',
    MIDDLEWARE_CLASSES=(
        "django.middleware.csrf.CsrfViewMiddleware",
    ),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        # 'django.contrib.webdesign',
        'nanodj',
        'contactform',
    ),
    STATIC_URL='/static/',
    STATIC_ROOT=None if NANO_DEBUG else os.path.join(BASE_PATH, "static"),
    STATICFILES_DIRS=[os.path.join(BASE_PATH, "static"), ],
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                os.path.join(BASE_PATH, "templates"),
            ],
            'APP_DIRS': True,
            'OPTIONS': {
                "context_processors": ["nanodj.context_processors.all_ipynb_pages", ]
            },
        },
    ],
    PAGE_SOURCE_DIR=os.path.join(BASE_PATH, "source"),
    PAGE_BUILD_DIR=os.path.join(BASE_PATH, "build"),
    # Needed for tests
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    },
    EMAIL_HOST=os.environ.get("NANO_EMAIL_HOST", None),
    EMAIL_PORT=os.environ.get("NANO_EMAIL_PORT", None),
    EMAIL_HOST_USER=os.environ.get("NANO_EMAIL_HOST_USER", None),
    EMAIL_HOST_PASSWORD=os.environ.get("NANO_EMAIL_HOST_PASSWORD", None),
    EMAIL_USE_TLS=os.environ.get("NANO_EMAIL_USE_TLS", None),
    EMAIL_RECIPIENTS=map(str.strip, os.environ.get("NANO_EMAIL_RECIPIENTS", "").split(","))
)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
else:
    from whitenoise.django import DjangoWhiteNoise
    application = get_wsgi_application()
    application = DjangoWhiteNoise(application)
