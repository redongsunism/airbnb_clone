from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):

    help = "This command creates amenities"

    # def add_arguments(self, parser):

    #     parser.add_argument(
    #         "--times", help="How many times do you want me to tell you that I love you?"
    #     )

    def handle(self, *args, **options):
        amenities = [
            "Kitchen",
            "Shampoo",
            "Heating",
            "Air conditioning",
            "Washer",
            "Dryer",
            "Wifi",
            "Breakfast",
            "Indoor fireplace",
            "Hangers",
            "Iron",
            "Hair dryer",
            "Laptop friendly workspace",
            "TV",
            "Crib",
            "High chair",
            "Self check-in",
            "Smoke detector",
            "Carbon monoxide detector",
            "Private bathroom",
            "Stereo",
            "Towels",
            "Toilet",
            "Sofa",
            "Microwave",
            "Restaurant",
            "Outdoor Pool",
            "Shopping Mall",
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))
