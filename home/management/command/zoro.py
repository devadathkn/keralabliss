from  django.core.management.base import BaseCommand
from django.utils import timezone
from home.models import tour 

class command(BaseCommand):
    help = 'Deletes Messmenu objects where day is in the past'

    def handle(self, *args, **kwargs):
        menudeleted = home.objects.filter(expiry_It=time.now())
        for m in menudeleted:
            m.delete()
        self.stdout.write (self.style.SUCCESS('successfully cleaned up MessMenu objects'))