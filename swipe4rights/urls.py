"""swipe4rights URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view

from accounts.viewsets import AccountViewSet
from bills.viewsets import BillViewSet
from votes.viewsets import VoteViewSet

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'bills', BillViewSet)
router.register(r'votes', VoteViewSet)

schema_view = get_swagger_view(title='Swipe4Rights API')

urlpatterns = [
    # API
    url(r'^api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns.append(url(r'^docs', schema_view))
