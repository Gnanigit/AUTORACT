# Generated by Django 4.1.1 on 2022-10-04 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KYCData', '0005_alter_details_dob_alter_details_fname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.BooleanField(default=True),
        ),
    ]
