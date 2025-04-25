from django.urls import path, include
from . import views

app_name = 'finlife'

urlpatterns = [
    path('save-deposit-products/',views.save_deposit_products,name = 'save-deposit-products'),
    # path('deposit-products/',views.deposit_products,name = 'deposit-products'),
    # path('deposit-product-options/<str:fin_prdt_cd>/',views.deposit_product_options,name ='deposit-product-options'),
    # path('deposit-products/top_rate/',views.top_rate,name='top_rate'),
]
