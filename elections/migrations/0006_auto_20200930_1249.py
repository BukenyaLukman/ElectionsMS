# Generated by Django 3.0.8 on 2020-09-30 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0005_auto_20200824_1438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='electionresult',
            old_name='VotesCasted',
            new_name='totalVoters',
        ),
        migrations.RemoveField(
            model_name='electionresult',
            name='totalVotes',
        ),
        migrations.AlterField(
            model_name='electionresult',
            name='resultsForm',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]