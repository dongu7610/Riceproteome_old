# Generated by Django 2.2.14 on 2022-06-11 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0058_projgetinfo_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectinfomodel',
            name='userlist',
            field=models.CharField(blank=True, max_length=2550),
        ),
    ]