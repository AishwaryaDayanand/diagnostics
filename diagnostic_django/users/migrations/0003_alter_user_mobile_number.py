# Generated by Django 4.1.2 on 2022-10-17 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_staff_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile_number',
            field=models.CharField(default=0, max_length=10),
        ),
    ]