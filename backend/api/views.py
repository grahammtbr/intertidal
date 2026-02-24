import json

from rest_framework import viewsets, generics
from core import models
from api import serializers
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.http import require_POST
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class SurveyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Survey.objects.all().order_by('start_date')
    serializer_class = serializers.SurveySerializer

class PersonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer

class RoleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Role.objects.all()
    serializer_class = serializers.RoleSerializer

# class DeploymentViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = models.Deployment.objects.all()
#     serializer_class = serializers.DeploymentSerializer

# Enables the ability to nest API routes, ie. /surveys/1/deployments/.
# DRF says they don't support nesting, but the reality is they do. See api/routes.py.
class DeploymentList(generics.ListAPIView):
    serializer_class = serializers.DeploymentSerializer

    # Initial relationship solution to filter by query pram, ie. /deployments/?survey=2
    # def get_queryset(self):
    #     queryset = models.Deployment.objects.all()
    #     survey = self.request.query_params.get('survey')
    #     if survey is not None:
    #         queryset = queryset.filter(survey_id = survey)
    #     return queryset

    # Works for URL relationship nesting. kwargs was key to getting the pk from the route.
    # https://docs.djangoproject.com/en/5.2/ref/urls/#kwargs
    def get_queryset(self):
        queryset = models.Deployment.objects.all().order_by('start_time')
        survey = self.kwargs.get('survey_id')
        if survey:
            queryset = queryset.filter(survey_id = survey)
        return queryset
    
class DeploymentDetail(generics.RetrieveAPIView):
    queryset = models.Deployment.objects.all()
    serializer_class = serializers.DeploymentSerializer

class GpsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Gps.objects.all()
    serializer_class = serializers.GpsSerializer

# class BaseDeploymentViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = models.BaseDeployment.objects.all()
#     serializer_class = serializers.BaseDeploymentSerializer

class BaseDeploymentList(generics.ListAPIView):
    serializer_class = serializers.BaseDeploymentSerializer

    def get_queryset(self):
        queryset = models.BaseDeployment.objects.all().order_by('start_time')
        deployment = self.kwargs.get('deployment_id')
        if deployment:
            queryset = queryset.filter(deployment_id = deployment)
        return queryset
    
class BaseDeploymentDetail(generics.RetrieveAPIView):
    queryset = models.BaseDeployment.objects.all()
    serializer_class = serializers.BaseDeploymentSerializer

class SurveyPointTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.SurveyPointType.objects.all()
    serializer_class = serializers.SurveyPointTypeSerializer

# class SurveyPointViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = models.SurveyPoint.objects.all()
#     serializer_class = serializers.SurveyPointSerializer

class SurveyPointList(generics.ListAPIView):
    serializer_class = serializers.SurveyPointSerializer

    def get_queryset(self):
        queryset = models.SurveyPoint.objects.all()
        base_deployment = self.kwargs.get('base_deployment_id')
        if base_deployment:
            queryset = queryset.filter(base_deployment_id = base_deployment)
        return queryset
    
class SurveyPointDetail(generics.RetrieveAPIView):
    queryset = models.SurveyPoint.objects.all()
    serializer_class = serializers.SurveyPointSerializer

class RasterTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.RasterType.objects.all()
    serializer_class = serializers.RasterTypeSerializer

class RasterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Raster.objects.all()
    serializer_class = serializers.RasterSerializer

# class RasterRpasFlightViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = models.RasterRpasFlight.objects.all()
#     serializer_class = serializers.RasterRpasFlightSerializer

# class RpasFlightViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = models.RpasFlight.objects.all()
#     serializer_class = serializers.RpasFlightSerializer

class RpasViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Rpas.objects.all()
    serializer_class = serializers.RpasSerializer

class RpasFlightList(generics.ListAPIView):
    serializer_class = serializers.RpasFlightSerializer

    def get_queryset(self):
        queryset = models.RpasFlight.objects.all().order_by('start_time')
        deployment = self.kwargs.get('deployment_id')
        if deployment:
            queryset = queryset.filter(deployment_id = deployment)
        return queryset
    
class RpasFlightDetail(generics.RetrieveAPIView):
    queryset = models.BaseDeployment.objects.all()
    serializer_class = serializers.BaseDeploymentSerializer

# --- Authorization ---

def get_csrf(request):
    response = JsonResponse({'detail': 'CSRF cookie set'})
    response['X-CSRFToken'] = get_token(request)
    return response


@require_POST
def login_view(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')

    if username is None or password is None:
        return JsonResponse({'success': False, 'detail': 'Please provide username and password.'}, status=400)

    user = authenticate(username=username, password=password)

    if user is None:
        return JsonResponse({'success': False, 'detail': 'You have provided an incorrect username or password. Please check your credentials and try again.'}, status=400)

    login(request, user)
    return JsonResponse({'success': True, 'username': username, 'detail': 'You have successfully logged in.'})


def logout_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'detail': 'You\'re not logged in.'}, status=400)

    logout(request)
    return JsonResponse({'detail': 'Successfully logged out.'})

class SessionView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, format=None):
        return JsonResponse({'isAuthenticated': True})


class WhoAmIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, format=None):
        return JsonResponse({'username': request.user.username})
