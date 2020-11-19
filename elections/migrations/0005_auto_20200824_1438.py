# Generated by Django 3.0.8 on 2020-08-24 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0004_remove_politiciancategory_constituency'),
    ]

    operations = [
        migrations.AddField(
            model_name='politicians',
            name='institution',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='politicians',
            name='education',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='PoliticianEducation',
        ),
    ]