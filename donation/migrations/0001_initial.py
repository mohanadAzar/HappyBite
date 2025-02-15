# Generated by Django 3.1.4 on 2020-12-13 00:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Packing_Type', models.CharField(choices=[('Packed', 'Packed'), ('Not Packed', 'Not Packed')], max_length=15)),
                ('Food_Type', models.CharField(max_length=20)),
                ('Donate_Date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('Expiry_Date', models.DateTimeField()),
                ('Available', models.BooleanField(default=True)),
                ('Deliver_Type', models.CharField(choices=[(' Delivery', ' Delivery'), ('No Delivery', 'No Delivery')], max_length=15)),
            ],
        ),
    ]
