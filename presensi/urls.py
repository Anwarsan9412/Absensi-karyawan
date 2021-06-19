from django.urls import path
from .views import CatPresensiView, AddAbsenView

urlpatterns = [
    path('<str:cats>/', CatPresensiView, name='presensi-cat'),
    # path('absen_hadir/', absens, name='abenss')
    # path('absen_hadir/', AddAbsenView.as_view(), name='add-absen' ),
    path('data-kehadiran/', AddAbsenView.as_view(), name='add-absen' )


]
