from django.conf.urls import url

from cart import views

urlpatterns = [
    url(r'', views.car_detail, name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove')
]

"""
URL  - Views - Template
localhost/cart/  - cart_detail - detail.html
localhost/cart/add/product_id/ - cart_add 
localhost/cart/remove/product_id/ - cart_remove
"""