import os
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import subprocess


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        for ipynb_file in os.listdir(settings.PAGE_SOURCE_DIR):
            full_path = os.path.join(settings.PAGE_SOURCE_DIR, ipynb_file)
            print full_path
            subprocess.Popen(
                # args=["--version",],
                args=["nbconvert", "--to=html", "--template=basic", full_path],
                cwd=settings.PAGE_BUILD_DIR,
                #
                executable="jupyter",
                shell=True
            )
