# Generated by Django 4.1 on 2022-08-08 12:29

import django.core.validators
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ("showroom", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="showroomcar",
            name="price",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                max_digits=8,
                validators=[django.core.validators.MinValueValidator(0.0)],
            ),
        ),
        migrations.AlterField(
            model_name="showroomprofile",
            name="balance",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                max_digits=8,
                validators=[django.core.validators.MinValueValidator(0.0)],
            ),
        ),
        migrations.AlterField(
            model_name="showroomprofile",
            name="location",
            field=django_countries.fields.CountryField(
                blank=True, max_length=2, null=True
            ),
        ),
    ]
