# Generated by Django 5.0.1 on 2024-02-22 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_anonymousreport_status_crimereportcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crimereport',
            name='status',
            field=models.CharField(default='Received', max_length=255),
        ),
    ]
