"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('logins',views.logins),
    path('logout',views.logout,name='logout'),
    path('hospital',views.hospitalindex,name='hospital'),
    path('user',views.userindex,name='user'),
    path('hospitalreg',views.hospitalreg),
    path('recieverreg',views.recieverreg),
    path('userprofile',views.userprofile,name='userprofile'),
    path('updat/<int:id>',views.updat, name='updat'),
    path('updat/updates/<int:id>',views.updates,name='updates'),
    path('hospitalprofile',views.hospitalprofile,name='hospitalprofile'),
    path('hospitalupdat/<int:id>',views.hospitalupdat,name='hospitalupdat'),
    path('hospitalupdat/hospitalupdates/<int:id>',views.hospitalupdates,name='hospitalupdates'),
    path('donor',views.donorpage,name='donor'),
    path('adddonors',views.adddonors, name="adddonors"),
    path('donoredit/<int:id>',views.donoredit,name='donoredit'),
    path('donoredit/donoredits/<int:id>',views.donoredits,name='donoredits'),
    path('donordelete/<int:id>',views.donordelete,name='donordelete'),
    path('donordetails/<int:id>',views.donordetails,name='donordetails'),
    path('addrequest',views.addrequest,name='addrequest'),
    path('viewrequest',views.viewrequest,name='viewrequest'),
    path('requestedlist',views.requestedlist,name='requestedlist'),
    path('requestaccept/<int:id>',views.requestaccept,name='requestaccept'),
    path('adddonor/<int:id>',views.adddonor,name='adddonor'),
    path('history',views.history,name='history'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
