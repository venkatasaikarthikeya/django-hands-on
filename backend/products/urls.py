from django.urls import path
from .views import *


urlpatterns = [
    path('', product_update_api_view),
    path('', product_list_create_api_view),
    path('<int:pk>/', product_detail_api_view),
]