# Generated by Django 4.1.2 on 2022-10-18 08:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0010_alter_appointment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='branch_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='Branch ID starts with MEDB', regex='^MEDB[0-9]{}')]),
        ),
    ]
