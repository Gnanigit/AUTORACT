# Generated by Django 4.1.1 on 2022-10-04 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KYCData', '0004_alter_details_dob_alter_details_fname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='dob',
            field=models.CharField(blank=True, max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='fname',
            field=models.CharField(blank=True, max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='gender',
            field=models.CharField(blank=True, max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='id_no',
            field=models.CharField(blank=True, max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='id_type',
            field=models.CharField(blank=True, max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='name',
            field=models.CharField(blank=True, max_length=122, null=True),
        ),
    ]
