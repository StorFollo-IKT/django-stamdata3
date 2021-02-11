import os

from django.test import TestCase

# Create your tests here.
from employee_info.load_data.LoadOrganisations import LoadOrganisations

from employee_info.models import Resource, Employment
from employee_info.management.commands.load_functions import Command

from employee_info.load_data.load_resources import LoadResources


class ResourceTestCase(TestCase):
    def setUp(self) -> None:
        folder = os.path.dirname(__file__)
        file = os.path.join(folder, 'test_data', 'stamdata_multi.xml')

        load_functions = Command()
        load_functions.handle()

        load_org = LoadOrganisations(file, 'AK')
        load_org.load()

        load = LoadResources(file, 'AK')
        load.load()

    def testMainPosition(self):
        resource = Resource.objects.get(resourceId=53453)
        main = resource.main_position()
        self.assertIsInstance(main, Employment)
