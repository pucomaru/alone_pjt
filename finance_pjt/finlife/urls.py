from django.urls import path, include
from . import views

app_name = 'finlife'

urlpatterns = [
    # 정기예금 상품 목록 DB에 저장장
    path('save-deposit-products/',views.save_deposit_products,name = 'save-deposit-products'),
    # 전체 정기예금금 상품 목력 출력 & 데이터 삽입입
    path('deposit-products/',views.deposit_products,name = 'deposit-products'),
    # 옵션들 저장
    path('save-deposit-options/',views.save_deposit_options,name = 'save-deposit-options'),
    # 특정 상품의 옵션 리스트 출력
    # path('deposit-product-options/<str:fin_prdt_cd>/',views.deposit_product_options,name ='deposit-product-options'),
    # 가입 기간에 상관없이 최고 ㄱㅁ리가 높은 금융 상품과 해당 상품의 옵련 리스트 출력
    # path('deposit-products/top_rate/',views.top_rate,name='top_rate'),
]
