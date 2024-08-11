from .views import *
from django.urls import path

urlpatterns = [

    # path('book', CalcualtionsAPIView.as_view()),
    path('print-bill/<int:booking_id>', PrintBill.as_view(),name='print-bill'),
    path('no-permission/', NoPermissionPage.as_view(), name='no_permission'),
    path('',HomePage.as_view())
]
