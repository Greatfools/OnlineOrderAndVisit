#coding: utf-8
from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
	# 主页
	url(r'^$', views.index, name = 'index'),
	# 登录
	url(r'^login', views.login, name = 'login'),
	# 注册
	url(r'^register', views.register, name = 'register'),
    # 个人信息查看页面
	url(r'myInfo/', views.myinfo, name = 'myInfo'),
	# header中搜索函数
	url(r'^search/$', views.search),
    #　以医院，科室为关键字的搜索列表
	url(r'^hospitalSearch/(?P<hospitalname>\w+)/$', views.hospitalSearch, name='hospitalSearch'),
	# 以医生为关键字的搜索列表
	url(r'^doctorSearch/(?P<doctorname>\w+)/$', views.doctorSearch, name='doctorSearch'),
	# 显示科室信息
	url(r'^officeinfo/o1([0-9]+)d2(.*)/$',views.officeinfo, name = 'officeinfo'),
	# 显示医院信息
    url(r'^hospital/$',views.hospital,name='hospital'),
	# 显示医生信息
	url(r'^doctor/$',views.doctor,name='doctor'),
	# 显示用户的预约信息
	url(r'^appointinfo/', views.appointInfo, name='appointinfo'),
	# 进行预约的处理函数，跳转到？
    url(r'^orderinfo/\((.+)L,\)/$', views.orderInfo, name='orderinfo'),
	# 取消预约，完成后跳转到？
	#url(r'^cancelInfo/', views.cancelInfo, name = 'cancelInfo'),
    url(r'^appointinfo/cpid23(.+)66',views.cancelInfo, name='cancelinfo'),
	# 进行支付， 完成后跳转到？
	#url(r'^payInfo/', views.payInfo, name = 'payInfo'),
    url(r'^appointinfo/cpid2(.+)366',views.payInfo, name='payinfo'),
    # 头部
	url(r'^header.html$', views.header, name = 'header'),
    #　尾部
    url(r'^footer.html$', views.footer, name ='footer'),
]

