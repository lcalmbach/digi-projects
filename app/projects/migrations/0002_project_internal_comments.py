# Generated by Django 5.1.4 on 2025-01-15 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='internal_comments',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Interne Bemerkungen'),
        ),
    ]
