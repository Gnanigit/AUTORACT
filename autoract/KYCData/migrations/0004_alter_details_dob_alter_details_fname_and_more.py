# Generated by Django 4.1.1 on 2022-10-04 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KYCData', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='dob',
            field=models.CharField(default=None, max_length=122),
        ),
        migrations.AlterField(
            model_name='details',
            name='fname',
            field=models.CharField(default=None, max_length=122),
        ),
        migrations.AlterField(
            model_name='details',
            name='gender',
            field=models.CharField(default=None, max_length=122),
        ),
        migrations.AlterField(
            model_name='details',
            name='id_no',
            field=models.CharField(default=None, max_length=122),
        ),
        migrations.AlterField(
            model_name='details',
            name='id_type',
            field=models.CharField(default=None, max_length=122),
        ),
        migrations.AlterField(
            model_name='details',
            name='name',
            field=models.CharField(default=None, max_length=122),
        ),
    ]
