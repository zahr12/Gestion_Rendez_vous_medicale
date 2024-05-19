from django.urls import path
from . import views

urlpatterns = [
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),

    path('api/patients/', views.PatientListCreateAPIView.as_view(), name='patient-list'),
    path('api/patients/<int:pk>/', views.PatientRetrieveUpdateDestroyAPIView.as_view(), name='patient-detail'),

    path('api/medecins/', views.MedecinListCreateAPIView.as_view(), name='medecin-list'),
    path('api/medecins/<int:pk>/', views.MedecinRetrieveUpdateDestroyAPIView.as_view(), name='medecin-detail'),

    path('api/rendezvous/', views.RendezVousListCreateAPIView.as_view(), name='rendezvous-list'),
    path('api/rendezvous/<int:pk>/', views.RendezVousRetrieveUpdateDestroyAPIView.as_view(), name='rendezvous-detail'),
]
