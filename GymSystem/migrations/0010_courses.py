# Generated by Django 3.0.5 on 2020-04-21 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GymSystem', '0009_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('price', models.CharField(max_length=100)),
            ],
        ),
    ]
