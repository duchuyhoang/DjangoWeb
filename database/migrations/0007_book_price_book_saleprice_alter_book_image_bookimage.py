# Generated by Django 4.0.2 on 2022-03-19 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_auto_20220313_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='salePrice',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
        migrations.CreateModel(
            name='BookImage',
            fields=[
                ('idBookImage', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(null=True, upload_to='uploads/')),
                ('idBook', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.book')),
            ],
            options={
                'db_table': 'book_image',
            },
        ),
    ]
