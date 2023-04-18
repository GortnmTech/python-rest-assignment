
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static



from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('profiles.urls')),
    path('posts/', include('posts.urls')),
    path('docs/', schema_view),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
