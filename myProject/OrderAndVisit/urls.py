from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
	# index
	url(r'^$', views.index, name = 'index'),
	# login operation, jump to index
	url(r'^login', views.login, name = 'login'),
	# register operation, jump to index
	url(r'^register', views.register, name = 'register'),
	# 搜索
	url(r'^search/$', views.search),

	url(r'^hospitalSearch/(?P<hospitalname>\w+)/$', views.hospitalSearch, name='hospitalSearch'),
	
	url(r'^doctorSearch/(?P<doctorname>\w+)/$', views.doctorSearch, name='doctorSearch'),
	# 显示科室信息
	url(r'^officeinfo/$',views.officeinfo, name = 'officeinfo'),
	# 显示医院信息
    url(r'^hospital/$',views.hospital,name='hospital'),
	# 显示医生信息
	url(r'^doctor$',views.doctor,name='doctor'),

	url(r'^myinfo$', views.myinfo, name='myinfo'),
	# 显示预约信息
	url(r'^appointinfo/', views.appointInfo, name='appointinfo'),
	
	# 进行预约，完成后跳转到？
	url(r'^orderInfo/', views.orderInfo, name = 'orderInfo'),
	# 取消预约，完成后跳转到？
	url(r'^cancelInfo/', vies.cancelInfo, name = 'cancelInfo');
	# 进行支付， 完成后跳转到？
	url(r'^payInfo/', views.payInfo, name = 'payInfo'),
	
	# 测试用
    url(r'^hello$', views.hello, name='hello'),
    # 测试搜索用
	url(r'^header/$', views.header, name = 'header'),
]