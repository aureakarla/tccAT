from django.contrib import admin
from django.urls import path, include
from noticias.views import index, depoimento_cadastro, forum
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('especies/', include('especies.urls')),
    path('noticias/', include('noticias.urls')),
    path('users/', include('users.urls')),
    path('forum/depoimentos/', depoimento_cadastro, name='depoimentos'),
    path('forum/', forum, name='forum-form'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
