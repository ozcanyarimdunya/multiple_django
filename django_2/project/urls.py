from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

index = TemplateView.as_view(template_name='index.html')
about = TemplateView.as_view(template_name='about.html')

urlpatterns = [
    path('v2/', index, name='index'),
    path('v2/about/', about, name='about'),
    path('v2/admin/', admin.site.urls),
]
