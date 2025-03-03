import json
from django.core.management.base import BaseCommand
from api.models import Region, District, Quarter


class Command(BaseCommand):
    help = 'Viloyat, tuman va mahallalarni JSON fayldan yuklash'

    def handle(self, *args, **kwargs):
        with open('regions.json', encoding='utf-8') as f:
            data = json.load(f)

        # Viloyatlarni yuklash
        for region_data in data['regions']:
            region, created = Region.objects.get_or_create(
                id=region_data['id'],
                defaults={'name': region_data['name']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Yangi viloyat qo'shildi: {region.name}"))

        # Tumanlarni yuklash
        for district_data in data['districts']:
            region = Region.objects.get(id=district_data['region_id'])
            district, created = District.objects.get_or_create(
                id=district_data['id'],
                defaults={'name': district_data['name'], 'region': region}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Yangi tuman qo'shildi: {district.name}"))

        # Mahallalarni yuklash
        for quarter_data in data['quarters']:
            district = District.objects.get(id=quarter_data['district_id'])
            quarter, created = Quarter.objects.get_or_create(
                id=quarter_data['id'],
                defaults={'name': quarter_data['name'], 'district': district}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Yangi mahalla qo'shildi: {quarter.name}"))
