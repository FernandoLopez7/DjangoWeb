from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # CRUD1
    path('usercreate', views.usercreate, name='usercreate'),
    path('userdetails/<int:id>', views.userdetails, name='userdetails'),
    path('useredit/<int:id>', views.useredit, name='useredit'),
    path('userdelete/<int:id>', views.userdelete, name='userdelete'),
    
    # Login, logout and register
    path('logout/',views.exit, name='exit'),
    path('iniciarsesion/',views.login_or_register, name='login_or_register'),
    
    # Mini core
    path('clientes/',views.indexclientes, name='clientes'),
    path('clientes/create/',views.clientescreate, name='clientescreate'),
    
    path('contratos/',views.indexcontratos, name='contratos'),
    path('contratos/create/',views.contratoscreate, name='contratoscreate'),
    
    path('reporte/', views.report, name='reporte'),
]