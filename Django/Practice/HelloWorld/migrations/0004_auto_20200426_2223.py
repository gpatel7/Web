# Generated by Django 2.1.5 on 2020-04-26 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HelloWorld', '0003_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='flights',
            field=models.ManyToManyField(blank=True, related_name='passangers', to='HelloWorld.Flight'),
        ),
    ]