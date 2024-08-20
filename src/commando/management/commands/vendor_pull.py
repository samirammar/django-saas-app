from typing import Any
from helpers import download_to_local
from django.core.management.base import BaseCommand
from django.conf import settings

VENDOR_STATICFILES = {
    "flowbite.min.css":"https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.css",
    "flowbite.min.js":"https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.js"
}


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        self.stdout.write("Downloading vendor static files.")
        completed_urls = []
        for name,url in VENDOR_STATICFILES.items():
            download = download_to_local(url, getattr(settings, 'STATICFILES_VENDOR_DIR') / name)
            if download:
                completed_urls.append(url)
            else:
                self.stdout.write(
                    self.style.ERROR(f'Failed to download {url}')
                )
        
        if set(completed_urls) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(
                self.style.SUCCESS(f'Successfully updated all static vendor static files.')
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'Some files were not updated.')
            )

        