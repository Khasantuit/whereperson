from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Region, District, Quarter, Person
from .serializers import RegionSerializer, DistrictSerializer, QuarterSerializer, PersonSerializer


# Region API
class RegionApiView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class RegionApiCreate(ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class RegionApiUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


# District API
class DistrictApiView(ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class DistrictApiCreate(ListCreateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class DistrictApiUpdate(RetrieveUpdateDestroyAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


# Quarter API
class QuarterApiView(ListAPIView):
    queryset = Quarter.objects.all()
    serializer_class = QuarterSerializer


class QuarterApiCreate(ListCreateAPIView):
    queryset = Quarter.objects.all()
    serializer_class = QuarterSerializer


class QuarterApiUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Quarter.objects.all()
    serializer_class = QuarterSerializer


# Person API
class PersonApiView(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonApiCreate(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonApiUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer