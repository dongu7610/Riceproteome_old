# Generated by Django 2.2.14 on 2022-03-31 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0045_analysisinfomodel_analysisinfotxt'),
    ]

    operations = [
        migrations.AddField(
            model_name='protein_calcultask',
            name='chrinfo',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]