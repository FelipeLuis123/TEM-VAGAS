from django.urls import path
from . import views

urlpatterns = [
    path('', views.destaques, name='main-page'),
    path('create-recommendation', views.create_recommendation, name='create-recommendation'),
    path('recommendation-detail/<int:id>/', views.recommendation_detail, name='recommendation-detail'),
    path('recommendation-update/<int:id>', views.recommendation_update, name='recommendation-update'),
    path('recommendation-delete/<int:id>/', views.recommendation_delete, name='recommendation-delete'),
]