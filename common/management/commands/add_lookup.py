# custom command/add_users.py
import csv
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
# from datetime import datetime
from django.utils.timezone import now
from common.models import ObjectLookUp

class Command(BaseCommand):
    help = 'Create look up values for administrative models.'

    def add_arguments(self, parser):
        parser.add_argument('--file_path', type=str, help='Path to the user data file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        timestamp = now() #datetime.now()

        with open(file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:

                ObjectLookUp.objects.create(
                    created_at=timestamp,
                    updated_at=timestamp,
                    is_active=True,
                    object_type=row['object_type'],
                    name=row['name'],
                    created_by_id=2,
                    updated_by_id=2
                )