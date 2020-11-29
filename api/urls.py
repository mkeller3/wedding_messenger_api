from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('authentication/get_token/', obtain_auth_token, name="get_token"),
    path('account/', views.account.as_view(), name="account"),
    path('guest/', views.guest.as_view(), name="guest"),
    path('guests/', views.guests.as_view(), name="guests"),
    path('group/', views.group.as_view(), name="group"),
    path('groups/', views.groups.as_view(), name="groups"),
    path('alert/', views.alert.as_view(), name="alert"),
    path('alerts/', views.alerts.as_view(), name="alerts"),
    path('send_text/', views.sendText.as_view(), name="send_text"),
    path('map_data/', views.mapData.as_view(), name="map_data"),
]
