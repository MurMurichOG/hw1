from django.urls import path
from . import views

urlpatterns = [
    path('female_clothes', views.FemaleClothes.as_view(), name='female_clothes'),
    path('pensioneer_clothes', views.PensioneerCLothes.as_view(), name='pensioneer_clothes'),
    path('male_clothes', views.MaleClothes.as_view(), name='male_clothes'),
    path('kids_clothes', views.KidsClothes.as_view(), name='kids_clothes')
]
