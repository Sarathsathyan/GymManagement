# Generated by Django 3.0.5 on 2020-04-26 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GymSystem', '0017_payments'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
