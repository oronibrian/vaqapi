from django.conf.urls import url,include
from django.contrib import admin
from Api import views




urlpatterns = [
     url(r'^login/$', views.userLoginViewSet.as_view(), name='login '),   
    # url(r'^(?P<pk>\d+)/$', views.JobViewSet.as_view(), name='jobs'),   

    

]
