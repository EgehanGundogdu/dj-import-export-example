from import_export import resources
from example.models import Driver



class DriverResource(resources.ModelResource):
    class Meta:
        model = Driver
