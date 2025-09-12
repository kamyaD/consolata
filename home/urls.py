from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('psychology-school/', views.psychology_school, name='psychology-school'),
    path('theology-school/', views.theology_school, name='theology-school'),
    path('philosophy-school/', views.philosophy_school, name='philosophy-school'),
    path('language-center/', views.language_center, name='language-center'),
    path('history/', views.history, name='history'),
    path('leadership/', views.leadership, name='leadership'),
    path('requirements/', views.requirements, name='requirements'),
   
]
