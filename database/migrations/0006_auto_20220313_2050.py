# Generated by Django 2.0.3 on 2022-03-13 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_auto_20220313_2037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='id_district',
            new_name='district',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='id_province',
            new_name='province',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='id_ward',
            new_name='ward',
        ),
    ]
