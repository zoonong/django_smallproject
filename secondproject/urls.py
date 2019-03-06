from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import blog.views

urlpatterns = [
    path('', blog.views.blog, name="blog"),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)