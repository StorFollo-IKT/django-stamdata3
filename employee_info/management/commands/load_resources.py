from datetime import datetime

from django.core.management.base import BaseCommand

from employee_info.load_data.load_resources import LoadResources
from employee_info.models import Company

now = datetime.now()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('company', nargs='+', type=str)

    def handle(self, *args, **options):
        company = options['company'][0]
        if company == 'all':
            companies = Company.objects.all()
        else:
            companies = [company]

        for company in companies:
            file = '/home/datagrunnlag/Stamdata3_teis_%s.xml' % company.companyCode

            load = LoadResources(file, company.companyCode)
            load.load()
