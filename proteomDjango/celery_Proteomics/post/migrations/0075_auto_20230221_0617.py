# Generated by Django 3.2 on 2023-02-21 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0074_auto_20221130_0557'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskidandID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Taskid', models.CharField(blank=True, max_length=255, null=True)),
                ('Analysisid', models.CharField(blank=True, max_length=255, null=True)),
                ('RelatedModels', models.CharField(blank=True, max_length=255, null=True)),
                ('finishmode', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='go_idinfo',
            name='Analysisid',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='protein_calcultask',
            name='Analysisid',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
