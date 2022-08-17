# Generated by Django 4.1 on 2022-08-17 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("car", "0001_initial"),
        ("dealer", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("showroom", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="transactionselltoshowroom",
            name="showroom",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="showroom.showroomprofile",
            ),
        ),
        migrations.AddField(
            model_name="dealerprofile",
            name="cars",
            field=models.ManyToManyField(through="dealer.DealerCar", to="car.car"),
        ),
        migrations.AddField(
            model_name="dealerprofile",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="dealercar",
            name="car",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="car.car"
            ),
        ),
        migrations.AddField(
            model_name="dealercar",
            name="dealer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="dealer.dealerprofile"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="dealercar",
            unique_together={("car", "dealer")},
        ),
    ]
