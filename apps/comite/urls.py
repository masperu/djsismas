from django.conf.urls import url

urlpatterns = [
    url(r'^listar$', "apps.administracion.views.HomeView", name="home"),
    url(r'^usuarios.usuario/listar/$', HomeView, name='user_list'),
    #url(r'^usuarios.usuario/crear/$', UsuarioCrear, name='user_add'),
]