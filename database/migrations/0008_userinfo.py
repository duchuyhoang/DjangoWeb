# Generated by Django 4.0.2 on 2022-04-10 10:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_book_price_book_saleprice_alter_book_image_bookimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.TextField(max_length=11)),
                ('avatar', models.ImageField(null=True, upload_to='uploads/')),
                ('birthday', models.DateField(default=datetime.datetime(2022, 4, 10, 17, 39, 58, 392379))),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='database.user')),
            ],
            options={
                'db_table': 'user_info',
            },
        ),
    ]