from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('prediction', views.prediction, name='prediction'),
    path('bupa_liver_prediction', views.bupa_liver, name='bupa_liver'),
    path('predictions/', views.predictions, name='dashboard-predictions'),
]
