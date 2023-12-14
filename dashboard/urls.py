from django.urls import path 
from .import views 

urlpatterns= [ 
 path('index.html/',views.index,name='index'),
 path('chart.html/',views.chart,name='chart'),
 path('widget.html/',views.widget,name='widget'),
 path('',views.login,name='login'),



 
 



]