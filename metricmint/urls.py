"""BPIBS12 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from stats.views import *
from adminpanel.views import *
from django.conf import settings 
from django.conf.urls.static  import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', recent,name='recent'),
    path('search/', searchengine,name='search'),
    path('notfound/', notfound,name='notfound'),
    path('infopage/<int:id>/', infopage,name='infopage'),
    path('statpage/<id>', statpage,name='statpage'),
    path('about/', about,name='about'),

    path('adminhome/',searched_words,name='adminhome'),
    path('country_add/', country_add,name='country_add'),
    path('country_upd/<int:id>/', country_upd,name='country_upd'),
    path('country_del/<int:id>/', country_del,name='country_del'),
    path('category_add/', category_add,name='category_add'),
    path('category_upd/<int:id>/', category_upd,name='category_upd'),
    path('category_del/<int:id>', category_del,name='category_del'),
    path('multiple_files_add/', multiple_files_add,name='multiple_files_add'),
    path('multiple_files_del/<int:id>/', multiple_files_del,name='multiple_files_del'),
    path('statcsv_add/', statcsv_add,name='statcsv_add'),
    path('statcsv_upd/<int:id>/', statcsv_upd,name='statcsv_upd'),
    path('statcsv_del/<int:id>/', statcsv_del,name='statcsv_del'),
    path('statpoint_add/', statpoint_add,name='statpoint_add'),
    path('statpoint_upd/<int:id>/', statpoint_upd,name='statpoint_upd'),
    path('statpoint_del/<int:id>/', statpoint_del,name='statpoint_del'),
    path('infolink_add/', infolink_add,name='infolink_add'),
    path('infolink_upd/<int:id>/', infolink_upd,name='infolink_upd'),
    path('infolink_del/<int:id>/', infolink_del,name='infolink_del'),
    path('infodevice_add/', infodevice_add,name='infodevice_add'),
    path('infodevice_upd/<int:id>/', infodevice_upd,name='infodevice_upd'),
    path('infodevice_del/<int:id>/', infodevice_del,name='infodevice_del'),
    path('infodatabase_add/', infodatabase_add,name='infodatabase_add'),
    path('infodatabase_upd/', infodatabase_upd,name='infodatabase_upd'),
    path('infodatabase_del/<int:id>/', infodatabase_del,name='infodatabase_del'),
    path('code_enter',code_ent,name='code_enter'),
    path('code/',code_add,name='code'),
    path('codeupdate/<int:id>/', codeupdate,name='codeupdate'),

   
  
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


