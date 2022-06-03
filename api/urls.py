from rest_framework_nested import routers 
from django.urls import path, include
from . import views

# parent route
router = routers.SimpleRouter()
router.register('students', views.StudentViewSet)

#child route
students_router = routers.NestedSimpleRouter(router, 'students', lookup='student')
students_router.register('images', views.StudentImageViewSet, basename='student-images')

#combine urls of both routers
urlpatterns = [
    path('', include(router.urls)),
    path('', include(students_router.urls))
]
