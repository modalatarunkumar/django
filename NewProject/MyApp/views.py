from django.shortcuts import render,redirect
from django.http import HttpResponse
from MyApp.models import Sregister
# Create your views here.
def hi(self):
	return HttpResponse("<h1>Hai guys welcome to Django session</h1><br><br><h2>Hello guys</h2>")
def hai(self,name):
	return HttpResponse("<h1>Hai welcome : {}</h1>".format(name))
def hai(self,name,age):
	return HttpResponse("<h1>hi welcome : {} </h1>and age is : {}".format(name,age))
def hai(self,name,age,sal):
	return HttpResponse("<span style=color:red;background-color:green><h1>name : {}</h1></span><br><h2>age : {}</h2><br>sal : {}".format(name,age,sal))
def helo(request):
	return HttpResponse("Hello guys")
def details(self,fname,lname,age):
	return render(self,'samples.html',{'f':fname,'l':lname,'a':age})
def alerts(self):
	return HttpResponse('<script> alert("Hello Welcome")</script>')
def det(self,fname,lname,age,adhar,pno):
	return render(self,'det.html',{'f':fname,'l':lname,'a':age,'ad':adhar,'p':pno})
def reg(request):
	if request.method=="POST":
		name = request.POST['sname']
		year = request.POST['syear']
		branch = request.POST['branch']
		#print(name,year,branch)
		return render(request,'form.html',{'n':name,'y':year,'b':branch})
	return render(request,'reg.html')
def index(request):
	return render(request,'index.html')
def about(self):
	return render(self,'about.html')
def contact(self):
	return render(self,'contact.html')
def operations(request):
	k = Sregister.objects.all() # To get all records from db
	if request.method=="POST":
		u = request.POST['us']
		p = request.POST['pd']
		n = request.POST['sn']
		a = request.POST['sa']
		e = request.POST['se']
		cr = Sregister(sname=n,age=a,suname=u,spwd=p,semail=e)
		cr.save()
		return redirect('/')
	return render(request,'operations.html',{'sd':k})
def sview(request,sv):
	n = Sregister.objects.get(id=sv)
	return render(request,'stview1.html',{'em':n})
def supdate(request,u):
	m = Sregister.objects.get(id=u)
	if request.method=="POST":
		m.sname=request.POST['sname']
		m.age = request.POST['age']
		m.suname = request.POST['suname']
		m.semail = request.POST['semail']
		m.save()
		return redirect('/')
	return render(request,'sup1.html',{'st':m})
def sdelete(request,d):
	b = Sregister.objects.get(id=d)
	if request.method=="POST":
		b.delete()
		return redirect('/')
	return render(request,'sdel1.html',{'sd':b})