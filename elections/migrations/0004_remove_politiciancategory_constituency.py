# Generated by Django 3.0.8 on 2020-08-24 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0003_parties_acronym'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='politiciancategory',
            name='constituency',
        ),
    ]
