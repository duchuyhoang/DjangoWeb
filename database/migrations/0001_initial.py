# Generated by Django 2.0.3 on 2022-03-13 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id_address', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField()),
                ('type', models.TextField()),
            ],
            options={
                'db_table': 'district',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField()),
                ('type', models.TextField()),
            ],
            options={
                'db_table': 'province',
            },
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField()),
                ('type', models.TextField()),
                ('district_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.District')),
            ],
            options={
                'db_table': 'ward',
            },
        ),
        migrations.AddField(
            model_name='district',
            name='province_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Province'),
        ),
        migrations.AddField(
            model_name='address',
            name='id_district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.District'),
        ),
        migrations.AddField(
            model_name='address',
            name='id_province',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.Province'),
        ),
        migrations.AddField(
            model_name='address',
            name='id_ward',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.Ward'),
        ),
    ]
