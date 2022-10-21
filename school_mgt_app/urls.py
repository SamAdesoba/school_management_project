from django.urls import include, path
from rest_framework.routers import DefaultRouter

from school_mgt_app import views

app_name = 'school_mgt_app'

router = DefaultRouter()
router.register('SchoolAdmin', views.SchoolAdminViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
