from django.urls import path
from .views import (
    HomeView,
    ItemViewDetail, add_to_cart
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<slug>/', ItemViewDetail.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart')
]