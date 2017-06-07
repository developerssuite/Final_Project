from django.conf.urls import url, include
from . import views

app_name = 'products'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about_us/$', views.about_us, name='about_us'),
    url(r'^categories/$', views.categories, name='categories'),
    url(r'^contact_us/$', views.contact_us, name='contact_us'),
    url(r'^profile/(?P<user_name>.*)/$', views.profile, name='profile'),
    url(r'^all_products/(?P<user_name>.*)/$', views.load_more_user_products, name='user_products_all'),
    url(r'^detail/(?P<product_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^create_product/$', views.create_product, name='create_product'),
    url(r'^delete_product/(?P<product_id>[0-9]+)/$', views.delete_product, name='delete_product'),
    url(r'^edit_product/(?P<product_id>[0-9]+)/$', views.edit_product_page, name='edit_product_page'),
    url(r'^product_edited/(?P<product_id>[0-9]+)/$', views.edit_product, name='edit_product'),
    url(r'^home/$', views.submit_newsletter, name='submit_newsletter'),
    url(r'^search/$', views.search, name='search'),  # For showing drop down categories
    url(r'^filter/$', views.search_result, name='search_result'),  # For showing results of main search and filtering
    url(r'^main_search/$', views.main_search, name='main_search'),  # For Main searching in the navbar
    url(r'^more_products/(?P<category>.*)/$', views.load_more, name='load_more'),  # For Main searching in the navbar
    # url(r'^account_setting/(?P<user>.*)/$', views.account_setting, name='account_setting'),

]
