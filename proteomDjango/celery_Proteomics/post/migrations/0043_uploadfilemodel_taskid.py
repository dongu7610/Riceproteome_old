# Generated by Django 2.2.14 on 2022-03-22 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0042_auto_20220321_0759'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfilemodel',
            name='taskId',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
