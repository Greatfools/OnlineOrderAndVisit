# coding=utf-8
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response



from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context
from django.db import connection, models
import datetime, calendar
from  django.template.loader import get_template
import time

import datetime

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Create your views here.
# 主页
def index(request):
	return HttpResponse('hello world')

# 搜索
def search(request):
	if 'key' in request.GET:
		key = request.GET['key'] # q is an object submitted by front
		return HttpResponseRedirect('/OrderAndVisit/officeinfo/')# 样本，需要改变

# 测试搜索用
def header(request):
	return render_to_response('header.html')# 样本，需要改变

# 显示科室信息
def officeinfo(request,officeid,dateid):
	Week = ["日","一","二","三","四","五","六"]
	daytime = ["m","a","e"]
	o_id = officeid
	d_id = dateid
	o_id = 1
	d = Department.objects.get(id = o_id)
	h = Hospital.objects.get(id = d.hospitalId_id)
	s = datetime.datetime.today()
	w = datetime.datetime.now().weekday() + 1
	visitdate = []
	dateprint = []
	dateweek = []
	num = 1
	while num < 8:
		dateprint.append((s + datetime.timedelta(days=num)).strftime("%m月%d日"))
		visitdate.append((s + datetime.timedelta(days=num)).strftime("%Y-%m-%d"))
		dateweek.append(Week[(w+num)%7])
		num = num+1
	# alldoctor = Doctor.objects.filter(departmentId_id = 1)

	record = [[False for x in range(7)] for y in range(3)]
	for i in range(7):
		for j in range(3):
			if j == 0:
				time = "m"
			elif j == 1:
				time = "a"
			elif j == 2:
				time = "e"
			cursor = connection.cursor()
			cursor.execute("""
				SELECT Count(*) FROM OrderAndVisit_visitmessage
				WHERE doctorId_id in (
				SELECT id FROM OrderAndVisit_doctor
				WHERE departmentId_id = 1) AND
				visitDate = '%s' AND
				visitTime = '%s' AND
				restNumber > 0""" % (visitdate[i],time))

			row = cursor.fetchone()
			if row[0] > 0:
				record[j][i] = visitdate[i] + daytime[j]
			else:
				record[j][i] = ""
	if d_id:
		visitList = VisitMessage.objects.filter(visitDate=d_id[0:-1], visitTime=d_id[-1],
												doctorId__departmentId_id__exact=1, restNumber__gt = 0)
	else:
		visitList = []
	return render_to_response ('officeinfo.html',{"dateprint":dateprint,"dateweek":dateweek,
												  "morning":record[0], "afternoon":record[1],
												  "evening":record[2],"h":h, "d_id":d_id, "o_id":o_id,
												  "visitList":visitList})

# 显示医生信息，单独页面
def doctor(request):
	Week = ["日", "一", "二", "三", "四", "五", "六"]
	s = datetime.datetime.today()
	w = datetime.datetime.now().weekday() + 1
	visitdate = []
	dateprint = []
	dateweek = []
	num = 1
	while num < 8:
		dateprint.append((s + datetime.timedelta(days=num)).strftime("%m月%d日"))
		visitdate.append((s + datetime.timedelta(days=num)).strftime("%Y-%m-%d"))
		dateweek.append(Week[(w + num) % 7])
		num = num + 1
	#
	visitId = [[False for x in range(7)] for y in range(3)]
	for i in range(7):
		for j in range(3):
			if j == 0:
				time = "m"
			elif j == 1:
				time = "a"
			elif j == 2:
				time = "e"
			cursor = connection.cursor()
			cursor.execute("""
					SELECT id FROM OrderAndVisit_visitmessage
					WHERE doctorId_id in (
					SELECT id FROM OrderAndVisit_doctor
					WHERE departmentId_id = 1) AND
					visitDate = '%s' AND
					visitTime = '%s' AND
					restNumber > 0""" % (visitdate[i], time))

			row = cursor.fetchone()
			if row > 0:
				visitId[j][i] = row
			else:
				visitId[j][i] = False

			#

	doc = Doctor.objects.get(id='1')
	dep=Department.objects.get(id=doc.departmentId_id)
	hos=Hospital.objects.get(id=dep.hospitalId.id)

	vis = VisitMessage.objects.filter(doctorId=doc.id)
	vtime = []
	for v in vis:
		vtime.append(v.visitDate)

	fp=open('./templates/doctorinfo.html')
	t=Template(fp.read())
	fp.close()
	#t=get_template('doctorinfo.html')
	html = t.render(Context({'date': dateprint,'name':doc.name,'info':doc.introduction,'address':doc.address,'dep':dep.name,'hos':hos.name,'morning':visitId[0],'afternoon':visitId[1],'evening':visitId[2],'week':dateweek}))
	return HttpResponse(html)

#　显示医院信息，单独页面
def hospital(request):
	hos = Hospital.objects.get(id='1')
	dep = Department.objects.filter(hospitalId=hos.id).order_by("classinfo")
	cursor = connection.cursor()
	cursor.execute("""
					SELECT count( * )
					FROM `OrderAndVisit_doctor`
					WHERE departmentId_id
					IN (
					SELECT id
					FROM `OrderAndVisit_department`
					WHERE hospitalId_id ='%s')
					"""%(hos.id) )

	row = cursor.fetchall()
	cursor.execute("""
	SELECT count( * )
	FROM `OrderAndVisit_ordermessage`
	WHERE visitId_id
	IN (

	SELECT id
	FROM `OrderAndVisit_visitmessage`
	WHERE doctorId_id
	IN (

	SELECT id
	FROM `OrderAndVisit_doctor`
	WHERE departmentId_id
	IN (

	SELECT id
	FROM `OrderAndVisit_department`
	WHERE hospitalId_id = '%s'
	)
	)
	)
	""" % (hos.id))

	peopleNum = cursor.fetchall()

	#
	# rows= [[] for i in range(len(row))]
	# for department in dep:
	# 	for i in range(len(row)):
	# 		if department.classinfo==row[i-1]:
	# 			rows[i-1].append(department)
	# 			#

	fp=open('./templates/hosinfo.html')
	t=Template(fp.read())
	fp.close()

	#t=get_template('doctorinfo.html')
	html=t.render(Context({'name':hos.name,'address':hos.address,'phonenum':hos.phonenum,'docnum':row[0][0],'info':hos.introduction,'dep':dep,'peoplen':peopleNum[0][0]}))
	return HttpResponse(html)

# 预约挂号，处理函数，跳转到？
def orderInfo(request, vid):
	#debug 1 userid
	usrid=1
	#visitid=1
	#Debug 1
	visitid=vid
	o_time=time.strftime( ISOTIMEFORMAT, time.localtime(time.time()) )
	print o_time
	#credit
	#rest
	vis=VisitMessage.objects.filter(id=vid)
	usr=User.objects.filter(id=usrid)
	#update it
	#cursor = connection.cursor()
	#cursor.execute("SELECT COUNT(*) FROM OrderAndVisit_ordermessage GROUP BY visitId_id")
	#raw = cursor.fetchone()
	#cursor.close()
	#print raw
	if vis[0].restNumber > 0:
		if usr[0].creditLevel > 0:
			# if date < 7
			rnm=vis[0].restNumber
			VisitMessage.objects.filter(id=vid).update(restNumber=rnm-1)
			cursor = connection.cursor()
			cursor.execute("INSERT INTO OrderAndVisit_ordermessage(userId_id, visitId_id,ordertime) values (%s,%s,%s)",[usrid,visitid,o_time])
			#Error Dealing
			cursor.close()
			msg="预约成功"
		else:
			msg="预约失败"
	else:
		msg="预约失败"
	print usrid,vid,msg
	return HttpResponseRedirect('../../')

#　取消预约，处理函数，跳转到？
def cancelInfo(request, oid):
	o_time=time.strftime( ISOTIMEFORMAT, time.localtime(time.time()) )
	usrid=1 #debug
	visitid=oid
	#Check of time to be continued......
	#if order can be canceled
	buf=OrderMessage.objects.filter(id=oid)
	if usrid == buf[0].userId.id:
		OrderMessage.objects.filter(id=oid).update(isCanceled=True)
		ToBeCanceledOrder = OrderMessage.objects.filter(id=visitid)
		#SQL
		cursor = connection.cursor()
		cursor.execute("INSERT INTO OrderAndVisit_ordercancelmessage(orderId_id,cancelTime) values (%s,%s)",[visitid,o_time])
		cursor.close()
		#Cope with payment
	return HttpResponseRedirect('../')

#　支付订单，处理函数，跳转到？
def payInfo(request, oid):
	#visitid=request.POST.visitid
	visitid=oid #debug
	usrid = 1 #debug
	TF = OrderMessage.objects.filter(id=visitid)
	if usrid == TF[0].userId.id:
		OrderMessage.objects.filter(id=visitid).update(isPayed=True)
	return HttpResponseRedirect('http://kevinfeng.moe/pay.html')

# 用户预约信息，单独页面
def appointInfo(request):
	#release
	#s_userid = request.user.id
	#debug
	s_userid = 1
	#Name
	us = User.objects.get(id=s_userid)
	sex = us.sex
	username = us.userName
	print us.sex
	#id is unique
	print us.name
	orderinfo = OrderMessage.objects.filter(userId=s_userid)
	return render(request, 'appointinfo.html', {'user': us, 'appointinfo': orderinfo})

# 用户登录，处理函数，跳转主页
def login(request):
	errors = []
	if 'name' in request.GET and request.GET['name']:
		if 'password' in request.GET and request.GET['password']:
			userName = request.GET['name']
			userPassword = request.GET['password']
			res = User.objects.filter(name = userName)
			if not res:
				errors.append('no such people')
			else:
				if res.password == userPassword:
					request.session['member_id'] = res.id
					return HttpResponseRedirect('/index/?errorMessage=errors')
		else:
			errors.append('please input your password')
	else:
		errors.append('please input your name')
	if (errors):
		return HttpResponseRedirect('/index/?errorMessage=errors')

#　用户注销，处理函数，跳转主页
def logout(request):
	try:
		del request.session['member_id']
	except KeyError:
		pass
	return HttpResponse("You're logged out")

# 用户注册，处理函数，跳转主页
def register(request):
	errors = []
	if request.method == 'POST':
		if not request.POST.get('name', ''):
			errors.append('Enter a name')
		if not request.POST.get('gender', ''):
			errors.append('Enter a gender')
		if not request.POST.get('idNum', ''):
			errors.append('Enter an idNum')
		if not request.POST.get('birthdate',''):
			errors.append('Enter a birthdate')
		if not request.POST.get('password', ''):
			errors.append('Enter a password')
		if not request.POST.get('phoneNum', ''):
			errors.append('Enter a phoneNum')
		if not errors:
			name = request.POST['name']
			password = request.POST['password']
			sex = request.POST['gender']
			birthDate = request.POST['birthdate']
			idNum = request.POST['idNum']
			phoneNum = request.PSOT['phoneNum']
			user_tmp = User(name = name, password = password, sex = sex, birthday = birthDate, telephone = phoneNum, idCard = idNum)
			user_tmp.save();

			res = User.objects.filter(name = name)
			request.session['member_id'] = res.id
	# return where? i think it should be discussed
	return HttpResponseRedirect('/index/?errorMessage=errors')

# 医院列表，单独页面
def hospitalSearch(request,hospitalname):
    hospitals = Hospital.objects.filter(name__contains=hospitalname)
    # data = serializers.serialize("json", hospitals)
    # print data

    output = ""
    hospitalnum = 0
    for h in hospitals:
        hospitalnum += 1
        doctors = Doctor.objects.filter(departmentId__id=h.id)
        doctornum = 0
        for doctor in doctors:
            doctornum += 1

        orders = OrderMessage.objects.filter(visitId__doctorId__departmentId__id=h.id)
        ordernum = 0
        for order in orders:
            ordernum += 1
        output += "{},{},{},{},{},{}<br>\n".format(h.name,h.img,h.introduction,doctornum,ordernum,h.address)
    output += "find "+ '%d' % hospitalnum +" hospitals<br>\n"
    print output

    return HttpResponse("%s" % output)

# 医生列表，单独页面
def doctorSearch(request,doctorname):
    doctors = Doctor.objects.filter(name__contains=doctorname).prefetch_related()
    # data = serializers.serialize("json", doctors)
    # print data

    output = ""
    doctornum = 0
    for doctor in doctors:
        doctornum += 1
        output += "{},{},{},{},{}<br>\n".format(doctor.name,doctor.title,doctor.departmentId.hospitalId.name,doctor.departmentId.name,doctor.introduction)
    output += "find " +'%d' % doctornum + " doctors<br>\n"
    print output
    return HttpResponse("%s" % output)

#　用户信息，单独页面
def myinfo(request):
	if (not request.session['member_id']):
		user_id = request.session['member_id']
		res = User.objects.filter(id = user_id)
		ret = {
			'name': res.name,
			'sex': res.sex,
			'idCard': res.idCard,
			'telephone': res.telephone,
		}
		return render_to_response ('myinfo.html', ret)
