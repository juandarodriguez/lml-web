# Generated by Django 2.2.7 on 2019-11-17 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
