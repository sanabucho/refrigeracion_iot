# Generated by Django 3.2.16 on 2022-11-26 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiv1', '0002_datats_enchufao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datats',
            name='enchufao',
        ),
    ]
