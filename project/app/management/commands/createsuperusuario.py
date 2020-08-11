from django.core.management.base import BaseCommand

from decouple import config

from app.models import Usuario


class Command(BaseCommand):
    help = "Creates a superuser defined by environment variables"

    def handle(self, *args, **options):
        username = config("SU_USERNAME")
        email = config("SU_EMAIL")
        password = config("SU_PASSWORD")

        qs = Usuario.objects.filter(username=username)
        if not qs:
            Usuario.objects.create_superuser(username, email, password)
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully created superuser "{username}".'
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(f'Superuser "{username}" already created.')
            )
