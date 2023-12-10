from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name=""),
    path('register', views.register, name= "register"),
    path('login', views.login, name= "login"),
    path('logout', views.logout, name= "logout"),
    path('dashboard', views.dashboard, name= "dashboard"),
    path('create-resume', views.create_resume, name= "create-resume"),
    path('update-resume/<int:pk>', views.update_resume, name= "update-resume"),
    path('view-resume/<int:pk>', views.view_resume, name= "view-resume"),
    path('delete-resume/<int:pk>', views.delete_resume, name= "delete-resume"),
]