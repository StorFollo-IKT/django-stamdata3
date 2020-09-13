from datetime import datetime

from django.core.management.base import BaseCommand

from employee_info.load_data.load_resources import LoadResources

now = datetime.now()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('company', nargs='+', type=str)

    def handle(self, *args, **options):
        customer = options['company'][0]
        file = '/home/datagrunnlag/Stamdata3_teis_%s.xml' % customer

        load = LoadResources(file, customer)
        load.load()
