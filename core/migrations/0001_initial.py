# Generated by Django 5.0.1 on 2024-02-13 12:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoliceStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('latitude', models.CharField(max_length=25)),
                ('longitude', models.CharField(max_length=25)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='WantedPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('alias', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('last_known_location', models.CharField(max_length=255)),
                ('offense', models.CharField(max_length=255)),
                ('contact_info', models.CharField(max_length=25)),
                ('image', models.ImageField(blank=True, null=True, upload_to='wanted')),
                ('status', models.CharField(max_length=25)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AnonymousReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crime_type', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('suspect_information', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('assigned_officer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='officer', to='management.user')),
            ],
        ),
        migrations.CreateModel(
            name='AnonymousAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='anonymous')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('crime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.anonymousreport')),
            ],
        ),
        migrations.CreateModel(
            name='CrimeReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crime_type', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('suspect_information', models.CharField(max_length=255)),
                ('witness_information', models.CharField(max_length=255)),
                ('reporter_cell', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('status', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('assigned_officer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_officer', to='management.user')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reporter', to='management.user')),
            ],
        ),
        migrations.CreateModel(
            name='CrimeAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='crime report')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('crime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.crimereport')),
            ],
        ),
    ]
