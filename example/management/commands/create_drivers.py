from django.core.management import BaseCommand
from example.models import Driver
import faker


class Command(BaseCommand):
    help = "Creates drivers."

    def add_arguments(self, parser):
        parser.add_argument("total", type=int, help="How many drivers will be created?")

    def handle(self, *args, **kwargs):
        total = kwargs.get("total")
        f = faker.Faker("tr_TR")
        drivers = [
            Driver(
                name=f.name(),
                plate_no=f.license_plate(),
                is_banned=f.boolean(),
                email=f.email(),
                started=f.date(),
            )
            for _ in range(total)
        ]
        Driver.objects.bulk_create(drivers)
        self.stdout.write(f"{total} drivers created.")
