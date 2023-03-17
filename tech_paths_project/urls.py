from django.urls import path
from .utils import import_abline_from_api
from .views import abline_list, abline_detail, abline_create, abline_update, abline_delete


urlpatterns = [
    path('', abline_list),
    path('create/', abline_create),
    path('import/', import_abline_from_api),
    path('<str:pk>/', abline_detail),
    path('<str:pk>/update/', abline_update),
    path('<str:pk>/delete/', abline_delete)
]

