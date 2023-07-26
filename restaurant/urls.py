from django.urls import path

from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('booking/', views.bookingview.as_view(), name='booking'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]