from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views


# Router with registered ViewSets. DRF DefaultRouter used to provide the API root overview.
# May change to SimpleRouter to set a custom base for initial FE loading.
router = DefaultRouter()
router.register(r'surveys', views.SurveyViewSet, basename='survey')
router.register(r'people', views.PersonViewSet, basename='person')
router.register(r'roles', views.RoleViewSet, basename='role')
#router.register(r'deployments', views.DeploymentList, basename='deployment')
router.register(r'gpses', views.GpsViewSet, basename='gps')
#router.register(r'base_deployments', views.BaseDeploymentViewSet, basename='base_deployment')
router.register(r'survey_point_types', views.SurveyPointTypeViewSet, basename='survey_point_type')
#router.register(r'survey_points', views.SurveyPointViewSet, basename='survey_point')
router.register(r'raster_types', views.RasterTypeViewSet, basename='raster_type')
#router.register(r'rasters', views.RasterViewSet, basename='raster')
#router.register(r'raster_rpas_flights', views.RasterRpasFlightViewSet, basename='raster_rpas_flight')
#router.register(r'rpas_flights', views.RpasFlightViewSet, basename='rpas_flight')
router.register(r'rpas', views.RpasViewSet, basename='rpas')

urlpatterns = [
    path('deployments/', views.DeploymentList.as_view()),
    path('surveys/<int:survey_id>/deployments/', views.DeploymentList.as_view()),
    path('deployments/<int:pk>/', views.DeploymentDetail.as_view()),

    path('base_deployments/', views.BaseDeploymentList.as_view()),
    path('deployments/<int:deployment_id>/base_deployments/', views.BaseDeploymentList.as_view()),
    path('base_deployments/<int:pk>/', views.BaseDeploymentDetail.as_view()),

    path('survey_points/', views.SurveyPointList.as_view()),
    path('base_deployments/<int:base_deployment_id>/survey_points/', views.SurveyPointList.as_view()),
    path('survey_points/<int:pk>/', views.SurveyPointDetail.as_view()),

    path('rpas_flights/', views.RpasFlightList.as_view()),
    path('deployments/<int:deployment_id>/rpas_flights/', views.RpasFlightList.as_view()),
    path('rpas_flights/<int:pk>/', views.RpasFlightDetail.as_view()),
    
    path('', include(router.urls)),
]
