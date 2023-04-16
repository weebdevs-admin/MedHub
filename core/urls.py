from django.urls import path
from .views import HomeTemplateView, AbautTemplateView,CourseTemplateView, Fundamental_Fanlar,CourseDepartament,CourseTheme,coursetypes,courseAbout,courseVideo,courseflash,coursetest


urlpatterns = [
    path('',HomeTemplateView.as_view(), name="home"),
    path('abaut', AbautTemplateView.as_view(), name='abaut'),
    path('course',CourseTemplateView.as_view(),name='course'),
    path('courses',Fundamental_Fanlar.as_view(),name='courses'),
    path('coursedepartament',CourseDepartament.as_view(),name='course_departament'),
    path('CourseTheme',CourseTheme.as_view(),name='course_theme '),
    path('coursetypes',coursetypes.as_view(),name='coursetypes'),
    path('courseAbout', courseAbout.as_view(),name="courseAbout"),
    path('courseVideo',courseVideo.as_view(),name="courseVideo"),
    path('courseflash',courseflash.as_view(),name="courseflash"),
    path('coursetest',coursetest.as_view(),name="coursetest")
]
