from django.contrib import admin
from django.urls import path,include
from . import views
app_name = 'shop'
urlpatterns = [
    path('',views.allProdCat,name='allProdCat'),
    path('contact/', views.contact, name='contact'),
    # path('contact/success/', views.contact_success, name='contact_success'),
    path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
    path('dress/<str:c_slug>/<str:product_slug>/', views.proDetail, name='procatdetail'),
     
]