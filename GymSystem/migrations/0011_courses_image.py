# Generated by Django 3.0.5 on 2020-04-21 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GymSystem', '0010_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]