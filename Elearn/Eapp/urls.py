from django.urls import path
from Eapp import views
from django.contrib.auth import views as ad


urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('',include('Eapp.urls')),
    path('',views.home,name='hm'),
    path('viw1/',views.about,name="ab"),
    path('ct1/',views.contact,name="co"),
    path('reg/',views.register,name="rg"),
    path('course/',views.Courselist,name="clist"),
    path('login/',ad.LoginView.as_view(template_name='login.html'),name='lg'),
    path('dashb/',views.dashboard,name="dsh"),
    path('logout/',ad.LogoutView.as_view(template_name='logout.html'),name='lgo'),
    path('profile/',views.profile1,name='prf'),
    path('pfupdate/',views.pfupdate1,name='pfup'),
    path('sample/',views.sample1),
    path('changepwd/',views.chpwd1,name="chpwd"),
]
