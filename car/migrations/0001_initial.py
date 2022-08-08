# Generated by Django 4.0.6 on 2022-08-08 11:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('engine', models.DecimalField(decimal_places=1, max_digits=2, validators=[django.core.validators.MinValueValidator(0.6), django.core.validators.MaxValueValidator(9.9)])),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1980), django.core.validators.MaxValueValidator(2021)])),
                ('color', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0.0)])),
            ],
        ),
    ]