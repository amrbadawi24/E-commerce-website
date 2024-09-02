from django.urls import path ,include
from . import views

urlpatterns = [
    path('check_out/',views.check_out,name="check_out"),
    path('update_shipping/',views.update_shipping,name="update_shipping"),
    path('create_shipping/',views.create_shipping,name="create_shipping"),
    path('billing_info/',views.billing_info,name="billing_info"),
    path('process_order/',views.process_order,name="process_order"),
    path('shipped_dash/',views.shipped_dash,name="shipped_dash"),
    path('not_shipped_dash/',views.not_shipped_dash,name="not_shipped_dash"),
    path('order_page<int:pk>',views.order_page,name="order_page"),
]
