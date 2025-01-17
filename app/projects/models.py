from django.db import models
from datetime import datetime

class Project(models.Model):
    title = models.CharField(verbose_name='Titel', max_length=200)
    decription = models.TextField(verbose_name='Beschreibung des Vorhabens', max_length=2000, blank=True, null=True)
    contact_person = models.CharField(verbose_name='Kontakt', max_length=100)
    description_before = models.TextField(verbose_name='Vorher', blank=True, null=True, max_length=1000)
    description_after = models.TextField(verbose_name='Nachher', max_length=1000)
    start_year = models.IntegerField(verbose_name='Von', default=datetime.now().year + 1)
    end_year = models.IntegerField(verbose_name='Bis', default=datetime.now().year)
    cost_plan_kchf = models.IntegerField(verbose_name='Budget (kCHF)', default=0)
    cost_effective_kchf = models.IntegerField(verbose_name="Ist-Kosten (kCHF)", default=0)
    effort_plan_pt = models.IntegerField(verbose_name="Aufwand Plan (PT)", default=0)
    duration_months = models.IntegerField(verbose_name="Dauer (Monate)" ,default=12)
    progress = models.IntegerField(verbose_name='Fortschritt (%)', default=0)

    process = models.IntegerField(verbose_name='Prozess (1-5)', default=0)
    kompetence = models.IntegerField(verbose_name='Kompentenz (1-5)', default=0)
    culture = models.IntegerField(verbose_name='Kultur (1-5)', default=0)
    technology = models.IntegerField(verbose_name='Technologie 1-5)', default=0)
    data = models.IntegerField(verbose_name='Daten (1-5)', default=0)
    legal = models.IntegerField(verbose_name='Recht (1-5)', default=0)

    employees = models.BooleanField(verbose_name="Mitarbeitende", default=False)
    citizens = models.BooleanField(verbose_name="Bevölkerung", default=False)
    economy = models.BooleanField(verbose_name="Wirtschaft", default=False)

    verwendung_portal = models.BooleanField(verbose_name="Sichtbar in öff. Portal", default=False)   
    internal_comments = models.TextField(verbose_name='Interne Bemerkungen', blank=True, null=True, max_length=1000)
    
    def status(self):
        if self.progress == 100:
            return 'Abgeschlossen'
        elif self.progress > 0:
            return 'In Bearbeitung'
        else:
            return 'Geplant'
    
    def __str__(self):
        return self.title
