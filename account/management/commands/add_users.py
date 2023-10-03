# custom command/add_users.py
import csv
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
# from datetime import datetime
from django.utils.timezone import now
from account.models import User
from perms.signals import assign_group

class Command(BaseCommand):
    help = 'Create custom users from a data file'

    def add_arguments(self, parser):
        parser.add_argument('--file_path', type=str, help='Path to the user data file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        is_superuser = False
        is_staff = False
        is_active = True

        date_joined = now() #datetime.now()

        with open(file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:

                hashed_password = make_password(row['password'])

                user = User.objects.create(
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    email=row['email'],
                    password= hashed_password,
                    role=row['role'],
					is_superuser = is_superuser,
					is_staff = is_staff,
					is_active = is_active,
                    date_joined = date_joined
                )

                user.save()
                print(f'Debug: running assign_group now for user {user.first_name}')
                assign_group(sender=User, instance=user, created=True)