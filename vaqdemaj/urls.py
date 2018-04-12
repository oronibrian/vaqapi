"""vaqdemaj URL Configuration
"""
from django.conf.urls import url,include
from django.contrib import admin

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from Api import views
from Api import models
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token


from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='vaqdemaj API')
from django.views.generic.base import RedirectView



router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet,'user')
router.register(r'jobs', views.JobViewSet)
router.register(r'bid', views.BidsList)
router.register(r'notification', views.NotificationViewSet)
router.register(r'geolocation', views.GeolocationViewSet)
router.register(r'wallet', views.WalletViewSet)
router.register(r'transaction', views.TransactionsViewSet)
# router.register(r'login',views.userLoginViewSet,base_name='login')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    # url(r'^api-auth/', include('rest_framework.urls')),
    url(r'accounts/', include('django.contrib.auth.urls')),
    # url(r'^$', RedirectView.as_view(permanent=False, url='/api/'))
    url(r'^api/token/', obtain_jwt_token),
    url(r'^api/refresh-token/', refresh_jwt_token),

    # url(r'^login/$', views.userLoginViewSet.as_view(), name='login '),
    url(r'^registration/', include('rest_auth.registration.urls')),
    url(r'^user-auth/', include('rest_auth.urls')),

   



    

]
