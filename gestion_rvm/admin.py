from django.contrib import admin
from .models import Patient, Medecin, RendezVous

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display =["id","nom", "email", "telephone", "genre"]
    
@admin.register(Medecin)
class MedecinAdmin(admin.ModelAdmin):
    list_display =["id","nom", "email", "specialite"]
    
@admin.register(RendezVous)
class RendezVousAdmin(admin.ModelAdmin):
    list_display =["id","patient_id", "medecin_id", "date"]
    
