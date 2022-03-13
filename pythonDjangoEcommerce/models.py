from django.db import models

# Create your models here.


class Province(models.Model):
    id = models.CharField(max_length=8, unique=True, primary_key=True)
    name = models.TextField()
    type = models.TextField()

    class Meta:
        db_table = 'province'


class District(models.Model):
    id = models.CharField(max_length=8, unique=True, primary_key=True)
    name = models.TextField()
    type = models.TextField()
    province_id = models.ForeignKey(Province, on_delete=models.CASCADE)

    class Meta:
        db_table = 'district'


class Ward(models.Model):
    id = models.CharField(max_length=8, unique=True, primary_key=True)
    name = models.TextField()
    type = models.TextField()
    district_id = models.ForeignKey(District, on_delete=models.CASCADE)
    class Meta:
        db_table = 'ward'


class Address(models.Model):
    id_address = models.AutoField(primary_key=True)
    id_province = models.ForeignKey(
        Province, null=True, on_delete=models.SET_NULL)
    id_district = models.ForeignKey(
        District, null=True, on_delete=models.SET_NULL)
    id_ward = models.ForeignKey(Ward, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'address'
