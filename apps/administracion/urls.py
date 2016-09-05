from django.conf.urls import url
from apps.administracion.views import *

urlpatterns = [
    url(r'^$', VistaInicio , name="home"),
    # url(r'^home/$', VistaInicio , name="home"),
    url(r'^login/$', Login , name="login"),
    url(r'^logout/$', Logout , name="logout"),
    #url(r'^usuarios.usuario/crear/$', UsuarioCrear, name='user_add'),
]