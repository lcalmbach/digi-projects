# Generated by Django 5.1.4 on 2025-01-18 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_decription_alter_project_cost_effective_kchf_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='project',
            name='decription',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='Beschreibung des Vorhabens'),
        ),
    ]
