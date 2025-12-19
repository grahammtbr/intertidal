from rest_framework import serializers
from core import models


class DeploymentSerializer(serializers.ModelSerializer):
    #survey = SurveySerializer()

    class Meta:
        model = models.Deployment
        fields = '__all__'

class SurveySerializer(serializers.ModelSerializer):
    #deployments = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='deployment-detail')
    #deployments = DeploymentSerializer(many=True)

    class Meta:
        model = models.Survey
        fields = '__all__'
        #fields = ['id', 'name', 'note', 'start_date', 'end_date', 'deployments']

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Person
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Role
        fields = '__all__'

class GpsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Gps
        fields = '__all__'

class BaseDeploymentSerializer(serializers.ModelSerializer):
    gps = GpsSerializer()
    manager = PersonSerializer()

    class Meta:
        model = models.BaseDeployment
        fields = '__all__'

class SurveyPointTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SurveyPointType
        fields = '__all__'

class SurveyPointSerializer(serializers.ModelSerializer):
    survey_point_type = SurveyPointTypeSerializer()

    class Meta:
        model = models.SurveyPoint
        fields = '__all__'

class RasterTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RasterType
        fields = '__all__'

class RasterSerializer(serializers.ModelSerializer):
    type = RasterTypeSerializer()

    class Meta:
        model = models.Raster
        fields = '__all__'

class RasterRpasFlightSerializer(serializers.ModelSerializer):
    raster = RasterSerializer()

    class Meta:
        model = models.RasterRpasFlight
        fields = '__all__'

class RpasSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Rpas
        fields = "__all__"

class RpasFlightSerializer(serializers.ModelSerializer):
    rasters = RasterRpasFlightSerializer(many=True)
    rpas = RpasSerializer()

    class Meta:
        model = models.RpasFlight
        fields = '__all__'
