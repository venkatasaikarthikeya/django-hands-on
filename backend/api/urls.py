from django.urls import path, include
from .views import api_home, api_todo, TodoView


urlpatterns = [
    path('', api_home),
    path('todos/', TodoView.as_view()),
    path('products/', include('products.urls'))
]