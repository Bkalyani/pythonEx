from django.conf import settings
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
#from django.core.context_processors import csrf
from django.http import *
from django.core import serializers
from django.core.cache import cache
import urllib2
import json
import os,binascii
#from jinja2 import Environment, FileSystemLoader
from django.views.generic.base import View
#connection = Connection('localhost', 27017)
#db = connection['sse_db']
from models import *
from json import dumps, loads
from django.core.serializers.json import DjangoJSONEncoder
import json

from django.db.models import Max,Count

def jsonConvert(out):
	output = serializers.serialize('json', out)
	cat  = json.loads(output)
	o = []
	lenOutput = out.count()
	for i in range(0, lenOutput):
		o1 = cat[i]['fields']
		o.append(o1)
	return o

class jquerycbox(View):
	def get(self,request):
		return render_to_response('jquerycbox1.html')

	def post(self,request):
		Cls(Name=request.POST['UserName'],Id=request.POST['Id']).save()		
		return redirect('/saveData')
				
class saveData(View):
	def get(self,request):	
		data = Cls.objects.filter()
		if data.count()>0:
			data=jsonConvert(data)
			return render_to_response('retrive.html', {"Data":data})
		else:
		    return HttpResponse(dumps({"message":"data not exist","Status":"fail"})) 


class updateData(View):
	def get(self,request):
		return render_to_response('jquerycbox1.html')
	def post(self,request):
		print '=================='
		if request.POST['UserName']!='' and request.POST['Id']!='':
			Cls.objects.filter(Name=request.POST['UserName']).update(Name=request.POST['UserName'],Id=request.POST['Id'])
			return redirect('/saveData')
		else:
			return HttpResponse(dumps({"message":"check all values","Status":"fail"}))

class deleteData(View):
	def get(self,request):
		return render_to_response('jquerycbox1.html')
	def post(self,request):
		print '=================='
		Cls.objects.filter(Name=request.POST['UserName']).delete()
		return redirect('/saveData')


'''
	def post(self,request):
		data= Cls.objects.filter(Name=request.POST['UserName'],Id=request.POST['Id'])
		if data.count()>0:
			print data,'99999999999999999'
			Cls.objects.filter(Name=request.POST['UserName']).update(Name=request.POST['UserName'],Id=request.POST['Id'])
			return redirect('/saveData')
		else:
			return HttpResponse(dumps({"message":"data not exist","Status":"fail"})) '''


	
'''
class editData(View):
	def get(self,request):				
		return self.editdata(request.GET["UserName"],request.GET["Id"])
	def editdata(self,UserName,Id):	
		if UserName!="" and Id!="":	
			data= Cls.objects.filter(Name=UserName,Id=Id)
			if data.count()>0:
				print data,'ccccccccc'  
				Cls.objects.filter(Name=UserName).update(Name=UserName,Id=Id)
				#s={'message':'updated successfully','status':'success'}
				#print s,'data'
				#return HttpResponse(dumps(s))
				data1 = Cls.objects.filter()
				if data1.count()>0:
					print data1,'tttttttttt'  
					data=jsonConvert(data1)
					print dumps(data),'22222222'
					return render_to_response('retrive.html',{"Data":data})
				else:
					return HttpResponse(dumps({"message":"data not exist","Status":"fail"})) 	
			else:
			    return HttpResponse(dumps({"message":"data not exist","Status":"fail"})) 
		else:
			return HttpResponse(dumps({"message":"check all values","Status":"fail"}))	'''




'''
class saveData(View):
	def saveData(self,request):	
       		print 'ddddddddddd'	
		data = Cls.objects.filter()
                if data.count()>0:
                        print data,'yyyyyyyyyy'  
	                data=jsonConvert(data)
	                print dumps(data),'gggggggggg'
	                return render_to_response('retrive.html', {"Data":data})
			#return HttpResponse(dumps({"message":data,"Status":"success"}))
                else:
                    return HttpResponse(dumps({"message":"data not exist","Status":"fail"})) '''
		