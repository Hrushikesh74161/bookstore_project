from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # user management
    path('accounts/', include('allauth.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),  # new
    # path('accounts/', include('users.urls')),  # new
    # local apps
    path('', include('pages.urls')),  # new
    path('books/', include('books.urls'))  # new
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # new