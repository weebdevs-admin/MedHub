from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
# Create your views here.





class HomeTemplateView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):

        
        context = super().get_context_data(**kwargs)  # first, call super get context data
        context['comment'] = Comment.objects.all()
        context['team'] = Team.objects.all()
        context['statistic'] = Statistic.objects.all()
        
        return context
class AbautTemplateView(TemplateView):
    template_name = 'aboutUs.html'


class CourseTemplateView(TemplateView):
    template_name = 'courseCategory.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # first, call super get context data
        context['coursecategory'] = CourseCategory.objects.all()
        
        return context


class Fundamental_Fanlar(TemplateView):
    template_name = "courses.html"



class CourseDepartament(TemplateView):
    template_name = 'courseDepartment.html'


class CourseTheme(TemplateView):
    template_name = 'courseTheme.html'


class coursetypes(TemplateView):
    template_name = 'coursetypes.html'



class courseAbout(TemplateView):
    template_name = 'courseAbout.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # first, call super get context data
        context['Asosiy_Malumotlar'] = Asosiy_Malumotlar.objects.all()
        
        return context






class courseVideo(TemplateView):
    template_name = "courseVideo.html"

    
class courseflash(TemplateView):
    template_name="courseflash.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # first, call super get context data
        context['Fleshcardlar'] = Fleshcardlar.objects.all()
        
        return context



class coursetest(TemplateView):
    template_name = 'coursetest.html'