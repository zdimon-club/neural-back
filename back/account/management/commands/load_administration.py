from django.core.management.base import BaseCommand, CommandError
from account.models import UserProfile
from django.contrib.auth.models import User
from back.settings import DOMAIN, BASE_DIR
from django.core.files import File
import random
from django.utils.dateparse import parse_date
from django.contrib.auth.models import Group



def create_users():
    print('Creating....admin')
    #country = random.choice(COUNTRIES.keys())
    u = UserProfile()
    u.username = 'admin'
    u.set_password('1q2w3e')
    u.is_active = True
    u.is_staff = True
    u.is_superuser = True
    u.email = '%s@gmail.com' % 'admin'
    u.is_superuser = True
    u.gender = 'male'
    u.save()
    my_group = Group.objects.get(name='admin') 
    my_group.user_set.add(u)
    my_group = Group.objects.get(name='director') 
    my_group.user_set.add(u)
    my_group = Group.objects.get(name='manager') 
    my_group.user_set.add(u)
    my_group = Group.objects.get(name='moderator') 
    my_group.user_set.add(u)
    my_group = Group.objects.get(name='webmaster') 
    my_group.user_set.add(u)

    return u

class Command(BaseCommand):
    'Import administrations into DB'
    def handle(self, *args, **options):
        print('Importing admin users...')
        User.objects.filter(username='admin').delete()
        create_users()
        