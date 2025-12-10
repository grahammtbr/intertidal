# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class Survey(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)
    note = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'survey'


class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(unique=True, max_length=256)

    class Meta:
        db_table = 'people'


class Role(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=32)

    class Meta:
        db_table = 'role'


class Deployment(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64)
    note = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    # Relations
    survey = models.ForeignKey('Survey', related_name='deployments', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


    class Meta:
        db_table = 'deployment'


class Gps(models.Model):
    id = models.BigAutoField(primary_key=True)
    brand = models.CharField(max_length=32)
    model = models.CharField(max_length=64)
    note = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'gps'


class BaseDeployment(models.Model):
    id = models.BigAutoField(primary_key=True)
    note = models.TextField(blank=True, null=True)
    base_height = models.FloatField()
    antenna_height = models.FloatField()
    original_position = models.PointField(geography=True, blank=True, null=True)
    position = models.PointField(geography=True, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    # Relations
    deployment = models.ForeignKey('Deployment', on_delete=models.CASCADE)
    gps = models.ForeignKey('Gps', on_delete=models.RESTRICT)
    manager = models.ForeignKey('Person', on_delete=models.RESTRICT)

    class Meta:
        db_table = 'base_deployment'


class BaseDeploymentFile(models.Model):
    id = models.BigAutoField(primary_key=True)
    file = models.FileField(upload_to='base_deployments', blank=True, null=True) # FileField
    note = models.TextField(blank=True, null=True)

    # Relations
    base_deployment = models.ForeignKey(BaseDeployment, on_delete=models.CASCADE)
    type = models.ForeignKey('BaseDeploymentFileType', on_delete=models.RESTRICT, blank=True, null=True)

    class Meta:
        db_table = 'base_deployment_file'


class BaseDeploymentFileType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=32)
    note = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'base_deployment_file_type'


class SurveyPoint(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64)
    note = models.TextField(blank=True, null=True)
    original_point = models.PointField(srid=4326, dim=3)
    cd_point = models.PointField(srid=4326, dim=3)
    point = models.PointField(srid=4326, dim=3)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    # Relations
    base_deployment = models.ForeignKey(BaseDeployment, on_delete=models.CASCADE)
    survey_point_type = models.ForeignKey('SurveyPointType', on_delete=models.RESTRICT)

    class Meta:
        db_table = 'survey_point'


class SurveyPointType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=32)
    note = models.TextField(blank=True, null=True)
    marker_color = models.CharField(max_length=7)

    class Meta:
        db_table = 'survey_point_type'


class Rpas(models.Model):
    id = models.BigAutoField(primary_key=True)
    brand = models.CharField(max_length=32)
    model = models.CharField(max_length=64)
    note = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'rpas'


class RpasFlight(models.Model):
    id = models.BigAutoField(primary_key=True)
    altitude = models.FloatField()
    velocity = models.FloatField()
    camera_mode = models.CharField(max_length=2) # choices=CameraModeChoices.choices, default=CameraModeChoices.AUTO
    aperture = models.CharField(max_length=32, blank=True, null=True)
    shutter_speed = models.CharField(max_length=32, blank=True, null=True)
    iso = models.IntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    flight_path = models.LineStringField(geography=True, blank=True, null=True)
    flight_path_file = models.FileField(upload_to='flight_paths', blank=True, null=True) # FileField
    plan_name = models.CharField(max_length=64, blank=True, null=True)
    plan_geometry = models.PolygonField(geography=True, blank=True, null=True)
    plan_file = models.FileField(upload_to='plan_geometries', blank=True, null=True) # FileField
    home_point = models.PointField(geography=True, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    # Relations
    deployment = models.ForeignKey(Deployment, on_delete=models.CASCADE)
    rpas = models.ForeignKey(Rpas, on_delete=models.RESTRICT)

    class Meta:
        db_table = 'rpas_flight'


class RpasFlightRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    note = models.TextField(blank=True, null=True)

    # Relations
    flight = models.ForeignKey(RpasFlight, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.RESTRICT)
    role = models.ForeignKey(Role, on_delete=models.RESTRICT)

    class Meta:
        db_table = 'rpas_flight_role'


class Raster(models.Model):
    id = models.BigAutoField(primary_key=True)
    file = models.FileField(upload_to='raster_upload', unique=True, blank=True, null=True) # FileField
    size = models.IntegerField(default=0)
    resolution = models.FloatField(default=0)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    srid = models.IntegerField(default=0)
    bands = models.IntegerField(default=0)
    extent = models.PolygonField(geography=True, blank=True, null=True)
    tile_dir = models.CharField(unique=True, max_length=128)

    # Relations
    type = models.ForeignKey('RasterType', on_delete=models.RESTRICT)

    class Meta:
        db_table = 'raster'


class RasterRpasFlight(models.Model):
    id = models.BigAutoField(primary_key=True)

    # Relations
    raster = models.ForeignKey(Raster, related_name='flights', null=False, on_delete=models.CASCADE)
    rpas_flight = models.ForeignKey('RpasFlight', related_name='rasters', on_delete=models.CASCADE)

    class Meta:
        db_table = 'raster_rpas_flight'


class RasterType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=32)

    class Meta:
        db_table = 'raster_type'


class Contour(models.Model):
    id = models.BigAutoField(primary_key=True)
    file = models.FileField(upload_to='contours', unique=True, blank=True, null=True) # FileField
    geom = models.MultiLineStringField(geography=True, blank=True, null=True)
    resolution = models.FloatField()

    # Relations
    raster = models.ForeignKey('Raster', on_delete=models.RESTRICT)

    class Meta:
        db_table = 'contour'
