# Generated by Django 2.2.5 on 2020-02-04 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20200204_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='summary',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]