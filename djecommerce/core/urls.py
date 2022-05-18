from django.urls import path
from .views import (
    HomeView,
    ItemViewDetail
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<slug>/', ItemViewDetail.as_view(), name='product')
]