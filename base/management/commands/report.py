import csv
import datetime
from django.core.management.base import BaseCommand, CommandError

from base.models import Product
from base.templatetags.basetags import get_time


class Command(BaseCommand):
    help = 'show all products in csv file'

    def add_arguments(self, parser):
        parser.add_argument('--limit',
                            dest='limit',
                            default=4,
                            help='max number of shown products',
                            )

    def handle(self, *args, **options):
        limit = int(options.get('limit'))
        with open("reports/{}.csv".format(get_time("%Y-%m-%d")), 'w+') as report_file:
            writer = csv.writer(report_file)
            row = ['product name row']
            for items in Product.objects.all()[:limit]:
                row.append(items.Name)
            writer.writerow(row)
