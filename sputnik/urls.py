"""hub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  path('blog/', include(blog_urls))
"""
from django.urls import include
from django.contrib import admin
from django.views.generic import TemplateView
from django_distill import distill_path
from sputnik.views import *

def getNone():
    return None

urlpatterns = [
    # distill_path('admin/', admin.site.urls, distill_func=getNone),
    distill_path('', TemplateView.as_view(template_name="index.html"), name="home", distill_func=getNone),
    # distill_path('vantagens/', AdvantagesPageView.as_view(), name='advantages', distill_func=getNone),
    # distill_path('produtos/', PricingPageView.as_view(), name='pricing', distill_func=getNone),
    # distill_path('parceiros/', PartnersPageView.as_view(), name='partners', distill_func=getNone),
    # distill_path('contato/', ContactPageView.as_view(), name='contact', distill_func=getNone)
]
