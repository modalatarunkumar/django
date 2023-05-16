from django.shortcuts import render,redirect
from django.http import HttpResponse
from Eapp.forms import UsReg,Crcty,pfupd,ChPwd
from Eapp.models import CourseCategory,User
#from .models import Article
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
	return render(request,'home.html')

def about(self):
	return HttpResponse('<h2>welcome to about</h2>')

def contact(self):
	return HttpResponse("<h3>Welcome to contact</h3>")

def register(request):
	g = UsReg()
	if request.method == "POST":
		g = UsReg(request.POST)
		if g.is_valid():
			g.save()
			return g
			return redirect("/")
			#return redirect("thank_you.html/")
	return render(request,"register.html",{'h':g})
@login_required
def Courselist(request):
	m = CourseCategory.objects.all()
	if request.method == "POST":
		t = Crcty(request.POST)
		if t.is_valid():
			t.save()
			return redirect('/course')
	t = Crcty()
	return render(request,'crselt.html',{'g':t,'h':m})
@login_required
def dashboard(request):
	return render(request,'dashboard.html')

@login_required
def profile1(request):
	return render(request,'profile.html')

@login_required
def pfupdate1(request):
	j = User.objects.get(id=request.user.id)
	if request.method=="POST":
		g = pfupd(request.POST,request.FILES,instance=j)
		if g.is_valid():
			g.save()
			return redirect('/profile')
	g = pfupd(instance=j)
	return render(request,'pfupdate.html',{'h':g})
def sample1(self):
	return render(self,'sample.html')
@login_required
def chpwd1(request):
	if request.method=="POST":
		b=ChPwd(user=request.user,data=request.POST)
		if b.is_valid():
			b.save()
			return redirect('/login')
	b = ChPwd(user=request.user)
	return render(request,'chpwd.html',{'h':b})