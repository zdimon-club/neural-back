from django.core.management.base import BaseCommand, CommandError
from account.models import UserProfile
from online.models import UserOnline



class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Ctearing...')
        UserOnline.objects.all().delete()
        for u in UserProfile.objects.all():
            u.is_online = False
            u.save()
        
