from django.db import models
from django.utils import timezone



class Patient(models.Model):
    nom = models.CharField(max_length=100, verbose_name = "Patient Name",default='')
    email = models.EmailField(max_length=277, verbose_name = "Patient Email",default='')
    telephone = models.CharField(max_length=20)
    genre_choices = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]
    genre = models.CharField(max_length=10, choices=genre_choices)

    def __str__(self):
        return str(self.id)
    
class Medecin(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Médecin Name", default='')
    email = models.EmailField(max_length=277, verbose_name="Médecin Email", default='')
    specialite = models.CharField(max_length=100, verbose_name="Spécialité")
    # Autres champs pertinents pour le médecin
    def __str__(self):
        return str(self.id)

class RendezVous(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name="Date du rendez-vous")

    def __str__(self):
        return str(self.id)
