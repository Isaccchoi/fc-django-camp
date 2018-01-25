from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.product_list,name='product_list'), #메인 페이지 카테고리 뷰
    url(r'^(?P<category_slug>[-\w]+)/$',views.product_list,name='product_list_by_category'), #지정된 카테고리가 있을 때 카테고리 뷰
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.product_detail,name='product_detail'), #지정된 제품의 디테일 뷰
]

"""
URL - View - Template
localhost - product_list - list.html
localhost/slug/ - product_list - list.html
localhost/id/slug/ - product_detail - detail.html
"""