from django.urls import path
from . import views 

urlpatterns = [
    path('automate-stock', views.scrape_stock, name='stock'),
    path('stock-autocomplete/', views.StockAutoComplete.as_view(), name='stock_autocomplete'),
]