from django.db import models
from datetime import datetime


class Area(models.Model):
    title = models.CharField(verbose_name='Handlungsfeld', max_length=100)
    description = models.TextField(verbose_name='Beschreibung', blank=True, null=True, max_length=1000)
    color = models.CharField(verbose_name='Farbe', max_length=7, default='#007bff')
    icon = models.CharField(verbose_name='Icon', max_length=50, default='fas fa-cogs')
    
    def __str__(self):
        return self.title
    

class Goal(models.Model):
    area = models.ForeignKey('Area', on_delete=models.CASCADE, verbose_name='Handlungsfeld', related_name='area_goals')
    title = models.CharField(verbose_name='Ziel', max_length=100)
    description = models.TextField(verbose_name='Beschreibung', blank=True, null=True, max_length=1000)
    color = models.CharField(verbose_name='Farbe', max_length=7, default='#007bff')
    icon = models.CharField(verbose_name='Icon', max_length=50, default='fas fa-bullseye')

    def __str__(self):
        return self.title
    

class Project(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(6)]  # 0 to 5

    title = models.CharField(verbose_name='Titel', max_length=200)
    description = models.TextField(verbose_name='Beschreibung des Vorhabens', max_length=2000, blank=True, null=True)
    contact_person = models.CharField(verbose_name='Kontakt', max_length=100)
    description_before = models.TextField(verbose_name='Vorher', blank=True, null=True, max_length=1000)
    description_after = models.TextField(verbose_name='Nachher', max_length=1000)
    start_year = models.IntegerField(verbose_name='Von', default=datetime.now().year)
    end_year = models.IntegerField(verbose_name='Bis', default=datetime.now().year + 1)
    cost_plan_kchf = models.IntegerField(verbose_name='Budget (kCHF)', default=0)
    cost_effective_kchf = models.IntegerField(verbose_name="Ist-Kosten (kCHF)", default=0)
    effort_plan_pt = models.IntegerField(verbose_name="Aufwand Plan (PT)", default=0)
    duration_months = models.IntegerField(verbose_name="Dauer (Monate)" ,default=12)
    progress = models.IntegerField(verbose_name='Fortschritt (%)', default=0)

    infrastructure = models.IntegerField(verbose_name='Digitale Infrastruktur (1-5)', default=0)
    data = models.IntegerField(verbose_name='Daten (1-5)', default=0)
    process = models.IntegerField(verbose_name='Prozesse (1-5)', default=0)
    culture = models.IntegerField(verbose_name='Trans­formation & Kulturwandel (1-5)', default=0)
    
    employees = models.BooleanField(verbose_name="Mitarbeitende", default=False)
    citizens = models.BooleanField(verbose_name="Bevölkerung", default=False)
    economy = models.BooleanField(verbose_name="Wirtschaft", default=False)

    url = models.URLField(verbose_name='URL', blank=True, null=True)
    verwendung_portal = models.BooleanField(verbose_name="Sichtbar in öffentlichem Portal", default=False)   
    internal_comments = models.TextField(verbose_name='Interne Bemerkungen', blank=True, null=True, max_length=1000)
    
    def status(self):
        if self.progress == 100:
            return 'Abgeschlossen'
        elif self.progress > 0:
            return 'In Bearbeitung'
        else:
            return 'Geplant'
    
    def display(self, rating):
        result = ''
        for i in range(rating + 1):
            result += '<i class="fas fa-circle"></i>'
        for i in range(5 - rating):
            result += '<span class="fa fa-circle-o"></span>'
        print(result)
        return result
    
    @property
    def   infrastructure_display(self):
        return self.display(self.infrastructure)
    
    @property
    def data_display(self):
        return self.display(self.data)
    
    @property
    def process_display(self):
        return self.display(self.process)
    
    @property
    def culture_display(self):
        return self.display(self.culture)

    def __str__(self):
        return self.title


class ProjectGoal(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, verbose_name='Vorhaben', related_name='project_goals')
    goal = models.ForeignKey('Goal', on_delete=models.CASCADE, verbose_name='Ziel', related_name='goal_projects')
    description = models.TextField(verbose_name='Beschreibung', blank=True, null=True, max_length=1000)

    def __str__(self):
        return f'{self.project} - {self.goal}'