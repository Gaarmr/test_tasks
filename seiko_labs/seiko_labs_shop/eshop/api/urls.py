from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^product/$', views.ProductListView.as_view(), name='product_list'),
    re_path(r'^product/(?P<pk>\d+)/$', views.ProductDetailView.as_view(), name='product_detail'),
    re_path(r'^(?P<shop_id>\d+)/categories/(?P<category_id>\d+)/$', views.ProductListView.as_view(), name='product_list'),
    # re_path(r'^(?P<pk>\d+)/categories/(?P<pk>\d+)/(?P<pk>\d+)/$', views.ProductListView.as_view(), name='id_shop3'),


    # re_path(r'^product/(?P<pk>\d+)/enroll/$', views.ProductEnrollView.as_view(), name='product_enroll'),
]