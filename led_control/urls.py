
from django.contrib import admin
from django.urls import path
from LedApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginView, name="loginView"),
    path('main', views.mainView, name="mainView")
]
