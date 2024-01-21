from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('regsiter/', views.register, name='register'),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('event/', views.get_event, name='event'),
    path('add_event/', views.post_event, name='add_event'),
    path('mod_event/', views.mod_event, name='mod_event'),
    path('del_event/<str:name>/<int:id>',
         views.del_event, name='del_event'),
    path('upd_event/<str:name>/<int:id>',
         views.upd_event, name='upd_event'),
    path('details/<int:id>', views.details, name='details'),
    path('add_dashboard/<str:name>/<int:id>',
         views.add_dashboard, name='add_dashboard'),
    path('del_dashboard/<int:user_id>/<int:event_id>/<int:user_event_id>',
         views.del_dashboard, name='del_dashboard'),
    path('add_userdetails/', views.add_userdetails, name='add_userdetails'),
]
