from django.urls import path
from .views import (
    RegionApiView, RegionApiCreate, RegionApiUpdate,
    DistrictApiView, DistrictApiCreate, DistrictApiUpdate,
    QuarterApiView, QuarterApiCreate, QuarterApiUpdate,
    PersonApiView, PersonApiCreate, PersonApiUpdate
)

urlpatterns = [
    # Region URLs
    path('regions/', RegionApiView.as_view(), name='region-list'),
    path('regions/create/', RegionApiCreate.as_view(), name='region-create'),
    path('regions/<int:pk>/', RegionApiUpdate.as_view(), name='region-detail'),

    # District URLs
    path('districts/', DistrictApiView.as_view(), name='district-list'),
    path('districts/create/', DistrictApiCreate.as_view(), name='district-create'),
    path('districts/<int:pk>/', DistrictApiUpdate.as_view(), name='district-detail'),

    # Quarter URLs
    path('quarters/', QuarterApiView.as_view(), name='quarter-list'),
    path('quarters/create/', QuarterApiCreate.as_view(), name='quarter-create'),
    path('quarters/<int:pk>/', QuarterApiUpdate.as_view(), name='quarter-detail'),

    # Person URLs
    path('persons/', PersonApiView.as_view(), name='person-list'),
    path('persons/create/', PersonApiCreate.as_view(), name='person-create'),
    path('persons/<int:pk>/', PersonApiUpdate.as_view(), name='person-detail'),
]
