"""djangopwa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from . import version
from .apps.pwa import views as pwa_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', pwa_views.my_page, name='home'),
    path('offline/', pwa_views.offline, name='offline'),
    path('say-something/<str:key>', pwa_views.say_something, name='say_something'),
    path('random-response', pwa_views.random_response, name='random_response'),
    path('fill-dynamic-cache/<int:id>', pwa_views.fill_dynamic_cache, name='fill_dynamic_cache'),
    path('must-not-cache', pwa_views.must_not_cache, name='must_not_cache'),

    # The service worker cannot be in /static because its scope will be limited to /static.
    # Since we want it to have a scope of the full application, we rely on this TemplateView
    # trick to make it work.
    path(
        'sw.js',
        pwa_views.ServiceWorkerView.as_view(),
        name=pwa_views.ServiceWorkerView.name,
    ),
]
