# Generated by Django 5.1 on 2024-08-14 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='passport_letter',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='street',
            field=models.CharField(max_length=255),
        ),
    ]
