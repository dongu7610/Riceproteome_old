# Generated by Django 3.2 on 2023-03-23 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0078_remove_network_nodeinfomation_notinmergest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchnetwork',
            name='case',
        ),
        migrations.AddField(
            model_name='getfinnetwork',
            name='getprojectid',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
