from django.urls import path, include
from .views import reservation_list, reservation_close

app_name = 'manager'


urlpatterns = [
    path('', reservation_list, name='reservation_list'),
    path('update/<int:pk>/', reservation_close, name='reservation_close'),
]
