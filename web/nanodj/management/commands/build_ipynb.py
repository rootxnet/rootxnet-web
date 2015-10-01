import os
import subprocess
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if not os.path.exists(settings.PAGE_BUILD_DIR):
            os.mkdir(settings.PAGE_BUILD_DIR)

        for ipynb_file in os.listdir(settings.PAGE_SOURCE_DIR):
            full_path = os.path.join(settings.PAGE_SOURCE_DIR, ipynb_file)
            print full_path
            popen = subprocess.Popen(
                args=["nbconvert", "--to=html", "--template=basic", full_path],
                cwd=settings.PAGE_BUILD_DIR,
                executable="jupyter",
                shell=True,
                stdout=subprocess.PIPE
            )
            print popen.stdout.read()
