# Generated by Django 3.2.21 on 2023-11-17 14:46

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_order_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phonenumber',
            field=phonenumber_field.modelfields.PhoneNumberField(error_messages={'invalid': 'Het ingevoerde telefoonnummer is niet juist. Gebruik het formaat +31 6xxxxxxxx.'}, max_length=128, region=None),
        ),
    ]