# Generated by Django 4.1.3 on 2023-03-15 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_alter_buyer_phone_alter_buyer_pin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyer',
            old_name='pic4',
            new_name='pic',
        ),
    ]