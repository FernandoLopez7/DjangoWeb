"""WEB1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CRUD1.urls')),
    # Para usar el inicio de sesion pretederminado de Django
    # path('accounts/',include('django.contrib.auth.urls')),
]

urlpatterns += [
    path('', RedirectView.as_view(url='/app/')), # Redirect on root (works on production environment with gunicorn)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)