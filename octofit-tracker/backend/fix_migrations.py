import os
import django
from django.core.management import call_command

def fix_migrations():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "octofit_tracker.settings")
    django.setup()

    print("Creating migrations...")
    call_command("makemigrations", interactive=False)

    print("Applying migrations...")
    call_command("migrate", interactive=False)

if __name__ == "__main__":
    fix_migrations()
