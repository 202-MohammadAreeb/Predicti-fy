
from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('home',views.home,name="home"),
    path('result',views.result,name="result"),
    path('home_two',views.home_two,name="home_two"),
    path('result_two',views.result_two,name="result_two"),
    path('feedbackForm',views.feedbackForm,name="feedbackForm"),
    path('rating',views.rating,name="rating"),
    path('remediesD',views.remediesD,name="remediesD"),
    path('remediesH',views.remediesH,name="remediesH"),
    path('about',views.about,name="about"),
    path('appointmentH',views.appointmentH,name="appointmentH"),
    path('appointmentD',views.appointmentD,name="appointmentD"),
    path('bmi_calculator',views.bmi_calculator,name="bmi_calculator"),
    path('yoga',views.yoga,name="yoga"),
    path('diet',views.diet,name="diet"),
    path('lungs',views.lungs,name='lungs'),
    path('resultLungs',views.resultLungs,name='resultLungs'),
    path('Kidney',views.Kidney,name='Kidney'),
    path('resultKidney',views.resultKidney,name='resultKidney')
    
  
    
]
