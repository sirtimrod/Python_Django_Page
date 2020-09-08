from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', include('log_web.urls')),
    # path('', include(('log_web.urls'))),
    # path('log_web/', include('django.contrib.auth.urls')),
]
