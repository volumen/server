"""django_volumen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

# Import the new view we created
from volumen_main_app.views import HomeView
from volumen_status_app.views import StatusView


urlpatterns = [
    url(r'^$', HomeView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^status/', StatusView.as_view()),
    url(r'^browse/', include('volumen_podcast_browser_app.urls')),
    url(r'^user/', include('volumen_user_app.urls')),
    url(r'^player/', include('volumen_player_app.urls')),
    url(r'^help/', include('volumen_help_app.urls')),
    # handler404 = 'path.to.views.custom404'
]
