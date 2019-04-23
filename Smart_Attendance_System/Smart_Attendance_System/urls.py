from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^face_recognition/', include('face_recognition.urls')),
    url(r'^admin_cpanel/', include('admin_cpanel.urls')),
    url(r'^admin/', admin.site.urls),
    url('accounts/', include('accounts.urls')),
    url(r'^', include('home.urls')),     # Seperate App
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^disclaimer/', include('disclaimer.urls')),
    url(r'^privacy_policy/', include('privacy_policy.urls')),
    url(r'^contact_us/', include('contact_us.urls')),
    url(r'^videos/', include('videos.urls')),
    url(r'mark_attendance', include('mark_attendance.urls')),
    url(r'fetch_data', include('fetch_data.urls')),
    url(r'^terms_and_conditions', include('terms_and_conditions.urls')),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
