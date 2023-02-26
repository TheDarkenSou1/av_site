from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from account.views import login_view, registration_view, logout_view
from contact.views import contact_list, contact_close


urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', login_view, name='login'),
    path('registration/', registration_view, name='registration'),
    path('logout/', logout_view, name='logout'),

    path('', include('main_page.urls')),
    path('manager/', include('manager.urls'), name='manager'),
    path('manager/contact/', contact_list, name='contact_list'),
    path('update/<int:pk>/', contact_close, name='contact_close'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
