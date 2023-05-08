# Generated by Django 2.2.14 on 2022-05-10 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0052_auto_20220427_0844'),
    ]

    operations = [
        migrations.CreateModel(
            name='Networksinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=2550, null=True)),
                ('source', models.CharField(blank=True, max_length=2550, null=True)),
                ('target', models.CharField(blank=True, max_length=25500, null=True)),
                ('taskId', models.CharField(blank=True, max_length=250, null=True)),
                ('Analysisinfo', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='networks_idinfo',
            name='Analysisinfo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
