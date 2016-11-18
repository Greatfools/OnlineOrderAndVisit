from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length = 20)
    level = models.CharField(max_length = 10)
    address =  models.CharField(max_length = 100)
    introduction = models.TextField(null = True)

    def __unicode__(self):
        return self.name

class User(models.Model):
    userName = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    name = models.CharField(max_length = 20)
    sex = models.CharField(max_length = 4)
    idCard = models.CharField(max_length = 18)
    telephone = models.CharField(max_length = 11)
    creditLevel = models.IntegerField(default = 5)

    def __unicode__(self):
        return self.userName

class Department(models.Model):
    hospitalId = models.ForeignKey(Hospital)
    name = models.CharField(max_length = 20)
    introduction = models.TextField(null = True)

    def __unicode__(self):
        return self.name

class Doctor(models.Model):
    departmentId = models.ForeignKey(Department)
    name = models.CharField(max_length = 10)
    title = models.CharField(max_length = 20)
    introduction = models.TextField(null = True)

    def __unicode__(self):
        return self.name

class Admin(models.Model):
    userName = models.CharField(max_length = 20)
    userPassword = models.CharField(max_length = 20)

    def __unicode__(self):
        return self.userName

class VisitMessage(models.Model):
    doctorId = models.ForeignKey(Doctor)
    visitDate = models.DateTimeField(auto_now_add = True)
    visitTime = models.CharField(max_length = 16)
    maxNumber = models.IntegerField(default = 0)
    restNumber = models.IntegerField(default = 0)

    def __unicdoe__(self):
        return self.doctorId + self.visitDate

class OrderMessage(models.Model):
    userId = models.ForeignKey(User)
    visitId = models.ForeignKey(VisitMessage)
    orderTime = models.DateTimeField(auto_now_add=True)
    isPayed = models.BooleanField(default = False)
    isCancel = models.BooleanField(default = False)

    def __unicode__(self):
        return self.userId + self.visitId + self.orderTime

class RegisterMessage(models.Model):
    orderId = models.ForeignKey(OrderMessage)
    visitId = models.ForeignKey(VisitMessage)
    orderNum = models.IntegerField()

    def __unicode__(self):
        return self.orderNum

class OrderCancelMessage(models.Model):
    orderId = models.ForeignKey(OrderMessage)
    cancelTime = models.DateTimeField()

class PayMessage(models.Model):
    orderId = models.ForeignKey(OrderMessage)
    value = models.IntegerField()
    Type = models.CharField(max_length = 10)
    status = models.CharField(max_length = 20)