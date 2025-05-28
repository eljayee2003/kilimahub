from django.core.management.base import BaseCommand
from core.models import Post
from django.db.models import Count

class Command(BaseCommand):
    help = 'Boost visibility for underrepresented African regions'

    def handle(self, *args, **kwargs):
        underrepresented = Post.objects.values('user__country').annotate(
            total=Count('id')
        ).filter(total__lt=100)
        self.stdout.write("Underrepresented African countries:")
        for entry in underrepresented:
            self.stdout.write(f"{entry['user__country']}: {entry['total']}")
