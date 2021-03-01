from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models import F
from adminpanel.forms import *
from stats.forms import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.contrib import messages


def searched_words(request):
    sea = searchenter.objects.all().order_by('-d')
    request.session['info_id']=" "
    request.session['cd_code'] =" "
    request.session['cd_code1'] = " "
    filter_on = request.session['cd_code']
    return render(request,'adminhome.html',{'sea':sea})



def country_add(request):
    if request.method == "POST":
        coufrm = new_country(request.POST)
        print(coufrm.errors)
        if coufrm.is_valid():
            couli = country.objects.all ()
            coufrm.save()
            coufrm = new_country ()
            messages.success(request,'data is added')
            return render ( request , 'country_add.html' , context = {'coufrm' : coufrm , 'couli' : couli} )

        else:
            return HttpResponse("enter all details")
    else:
        coufrm = new_country()
        couli = country.objects.all ()
        return render(request, 'country_add.html', context= {'coufrm': coufrm,'couli':couli})


def country_upd(request,id):
        coupd=country.objects.get(id=id)
        coufrm =new_country(instance=coupd)
        if request.method=='POST':
            coufrm=new_country(request.POST,instance=coupd)
            print(coufrm.errors)
            if coufrm.is_valid():
                couli = country.objects.all ()
                coufrm.save()
                coufrm = new_country ()
                messages.success(request, 'data is updated')
                return render ( request , 'country_add.html' , context = {'coufrm' : coufrm , 'couli' : couli} )

            else:
                return HttpResponse("CORRECT YOUR DETAILS")
        else:
            coufrm =new_country(instance=coupd)
            couli = country.objects.all ()
            return render(request,'country_add.html',context={'coufrm':coufrm,'couli':couli})


def country_del(request,id):
    coudel=country.objects.get(id=id)
    coudel.delete()
    coufrm = new_country ()
    couli=country.objects.all()
    messages.success(request,  'data is deleted')
    return render ( request , 'country_add.html' , context={'coufrm':coufrm,'couli' : couli} )


def category_add(request) :
    if request.method == "POST" :
        catfrm = add_cat(request.POST)
        print(catfrm.errors)
        if catfrm.is_valid() :
            catfrm.save()
            catli = cat.objects.all ()
            catfrm = add_cat ()
            messages.success(request,'data is added')
            return render ( request , 'category_add.html' , context={'catfrm' : catfrm,'catli':catli} )
        else :
            return HttpResponse ( "enter all details" )
    else :
        catli = cat.objects.all ()
        catfrm = add_cat ()
        return render ( request , 'category_add.html' , context = {'catfrm' : catfrm , 'catli' : catli} )


def category_upd(request ,id) :
    catupd = cat.objects.get(id = id )
    catfrm = add_cat(instance = catupd )
    if request.method == 'POST' :
        catfrm = add_cat(request.POST,instance = catupd)
        print(catfrm.errors )
        if catfrm.is_valid () :
            catfrm.save ()
            catli = cat.objects.all ()
            messages.success ( request , 'data is updated' )
            return render ( request , 'category_add.html' , context = {'catfrm' : catfrm , 'catli' : catli} )

        else :
            return HttpResponse ( "CORRECT YOUR DETAILS" )
    else :
        catli = cat.objects.all ()
        catfrm = add_cat (instance= catupd)
        return render ( request , 'category_add.html' , context = {'catfrm' : catfrm , 'catli' : catli} )


def category_del(request , id) :
    catdel = cat.objects.get( id = id )
    catdel.delete ()
    catli = cat.objects.all ()
    catfrm = add_cat ()
    messages.success ( request , 'data is deleted' )
    return render ( request , 'category_add.html' , context = {'catfrm' : catfrm , 'catli' : catli} )

def code_ent(request):
    if request.method =="POST":
        codfrm = code_form(request.POST)
        if codfrm.is_valid():
            codfrm.save()
            return  redirect('multiple_files_add')
        else:
            return HttpResponse("same code")
    else:
        codfrm = code_form()
        mulli = Multiple_images.objects.all ().order_by('-date_inp')
        return render(request,'code_enter.html',context={'codfrm':codfrm, 'mulli' : mulli})




def multiple_files_add(request) :
    if request.method == "POST":
        mulfrm = mutiple_imagesselectform(request.POST, request.FILES)
        m_files= request.FILES.getlist('image')
        if mulfrm.is_valid():
            print(m_files)
            t_tittle=mulfrm.cleaned_data['tittle']
            cde= mulfrm.cleaned_data['code']
            check= Multiple_images.objects.filter(code=cde)
            if len(check) == 0:
                for f in m_files:
                    b=Multiple_images(tittle=t_tittle,image=f,code=cde)
                    b.save()

                mulli = Multiple_images.objects.all ().order_by('-date_inp')
                mulfrm = mutiple_imagesselectform ()
                messages.success(request,'data is added')
                return render ( request , 'multiple_files_add.html' ,context = {'mulfrm' : mulfrm , 'mulli' : mulli} )

            else:
                return HttpResponse("please write different code")

        else:
            return HttpResponse("wrong data")

    else:
        mulfrm=mutiple_imagesselectform()

        mulli = Multiple_images.objects.all ()
        return render(request,'multiple_files_add.html',context={'mulfrm':mulfrm,'mulli':mulli})



def multiple_files_del(request , id) :
    muldel = Multiple_images.objects.get( id = id )
    muldel.delete ()
    mulfrm = mutiple_imagesselectform ()
    mulli = Multiple_images.objects.all ()
    messages.success(request,'data is deleted')
    return render ( request , 'multiple_files_add.html' , context = {'mulfrm' : mulfrm , 'mulli' : mulli} )



def statcsv_add(request):
    if request.method == "POST":
        statscsvfrm = statfile_form(request.POST)
        print(statscsvfrm.errors)
        if statscsvfrm.is_valid():
            statscsvfrm.save()
            statscsvfrm = statfile_form ()
            statscsvli = stat.objects.exclude( s_csv__isnull = True )
            messages.success(request,'data is added')
            return render ( request , 'statscsv_add.html' , context = {'statscsvli' : statscsvli,'statscsvli':statscsvli} )
        else:
            return HttpResponse("enter correct details")
    else:
        statscsvfrm = statfile_form()
        statscsvli = stat.objects.exclude( s_csv__isnull = True)
        return render ( request , 'statscsv_add.html' , context = {'statscsvli' : statscsvli,'statscsvfrm': statscsvfrm} )





def statcsv_upd(request,id):
        statscsvupd=stat.objects.get(id=id)
        statscsvfrm=statfile_form(instance=statscsvupd)
        if request.method=='POST':
            statscsvfrm=statfile_form(request.POST,instance=statscsvupd)
            print(statscsvfrm.errors)
            if statscsvfrm.is_valid():
                statscsvfrm.save()
                statscsvfrm = statfile_form()
                statscsvli = stat.objects.exclude(s_csv__isnull = True)
                messages.success(request,'data is updated')
                return render ( request , 'statscsv_add.html' , context = {'statscsvli' : statscsvli , 'statscsvfrm' : statscsvfrm} )


            else:
                return HttpResponse("CORRECT YOUR DETAILS")
        else:
            statscsvfrm =statfile_form(instance=statscsvupd)
            statscsvli = stat.objects.exclude( s_csv__isnull = True)
            return render ( request , 'statscsv_add.html' ,context = {'statscsvli' : statscsvli , 'statscsvfrm' : statscsvfrm} )


def statcsv_del(request,id):
    statcsvdel=stat.objects.get(id=id)
    statcsvdel.delete()
    statscsvfrm = statfile_form ()
    statscsvli = stat.objects.exclude(s_csv__isnull = True)
    messages.success(request,'data is deleted')
    return render ( request , 'statscsv_add.html' ,context = {'statscsvli' : statscsvli , 'statscsvfrm' : statscsvfrm} )


def statpoint_add(request):
    if request.method == "POST":
        statpointfrm = statpoint_form(request.POST)
        print(statpointfrm.errors)
        if statpointfrm.is_valid():
            statpointfrm.save()
            statpointfrm = statpoint_form ()
            statpointli = stat.objects.exclude(x_pts__isnull = True)
            messages.success(request,'data is added')
            return render ( request , 'statpoint_add.html' , context = {'statpointli' : statpointli,'statpointfrm':statpointfrm} )
        else:
            return HttpResponse("enter correct details")
    else:
        statpointfrm = statpoint_form ()
        statpointli = stat.objects.exclude(x_pts__isnull = True)
        return render ( request , 'statpoint_add.html' , context = {'statpointli' : statpointli, 'statpointfrm':statpointfrm} )



def statpoint_upd(request,id):
        statpointupd=stat.objects.get(id=id)
        statpointfrm=statpoint_form(instance=statpointupd)
        if request.method=='POST':
            statpointfrm=statpoint_form(request.POST,instance=statpointupd)
            print(statpointfrm.errors)
            if statpointfrm.is_valid():
                statpointfrm.save()
                statpointfrm = statpoint_form ()
                statpointli = stat.objects.exclude(x_pts__isnull = True)
                messages.success(request, "data is updated")
                return render ( request , 'statpoint_add.html' ,context = {'statpointli' : statpointli , 'statpointfrm':statpointfrm} )
        else:
            statpointfrm =statpoint_form(instance=statpointupd)
            statpointli = stat.objects.exclude(x_pts__isnull = True)
            return render ( request , 'statpoint_add.html' ,context = {'statpointli' : statpointli , 'statpointfrm':statpointfrm} )


def statpoint_del(request,id):
    statpointdel=stat.objects.get(id=id)
    statpointdel.delete()
    statpointfrm = statpoint_form ()
    statpointli = stat.objects.filter (x_pts__isnull = True)
    messages.success(request,'data is deleted')
    return render ( request , 'statpoint_add.html' ,context = {'statpointli' : statpointli , 'statpointfrm':statpointfrm} )





def infolink_add(request):
    if request.method == "POST":
        infolinkfrm = infolink_form(request.POST)
        print(infolinkfrm.errors)
        if infolinkfrm.is_valid():
            try:
                infolinkfrm.save()
            except:
                pass
            infolinkli = infog.objects.filter(imageurl1__isnull = False)
            infolinkfrm =infolink_form()
            messages.success(request,'data is added')
            return render ( request , 'infolink_add.html' , context = {'infolinkfrm' : infolinkfrm, 'infolinkli':infolinkli} )
        else:
            return HttpResponse("enter correct details")
    else:
        infolinkfrm = infolink_form()
        infolinkli = infog.objects.filter(imageurl1__isnull = False)
        return render ( request , 'infolink_add.html' , context = {'infolinkfrm' : infolinkfrm, 'infolinkli':infolinkli} )



def infolink_upd(request,id):
        infolinkupd=infog.objects.get(id=id)
        infolinkfrm=infolink_form(instance=infolinkupd)
        if request.method=='POST':
            infolinkfrm=infolink_form(request.POST,instance=infolinkupd)
            print(infolinkfrm.errors)
            if infolinkfrm.is_valid():
                try:
                    infolinkfrm.save()
                except:
                    pass
                infolinkli = infog.objects.filter(imageurl1__isnull = False)
                infolinkfrm =infolink_form()
                messages.success(request,'data is updated')
                return render ( request , 'infolink_add.html' , context = {'infolinkfrm' : infolinkfrm, 'infolinkli':infolinkli} )
            else:
                return HttpResponse("CORRECT YOUR DETAILS")
        else:
            infolinkfrm =infolink_form(instance=infolinkupd)
            infolinkli = infog.objects.filter(imageurl1__isnull = False)
            return render (request , 'infolink_add.html' , context = {'infolinkfrm' : infolinkfrm, 'infolinkli':infolinkli})


def infolink_del(request,id):
    infolinkdel=stat.objects.get(id=id)
    infolinkdel.delete()
    infolinkfrm =infolink_form()
    infolinkli = infog.objects.filter(imageurl1__isnull = False)
    messages.success(request,'data is deleted')
    return render ( request , 'infolink_add.html' , context = {'infolinkfrm' : infolinkfrm, 'infolinkli':infolinkli} )



def infodevice_add(request):
    if request.method == "POST":
        infodevicefrm = infodevice_form(request.POST,request.FILES)
        print(infodevicefrm.errors)
        if infodevicefrm.is_valid():
            infodevicefrm.save()
            infodeviceli = infog.objects.filter(i_image__isnull = False)
            infodevicefrm =infodevice_form()
            messages.success(request,'data is added')
            return render ( request , 'infodevice_add.html' , context = {'infodevicefrm' : infodevicefrm,'infodeviceli':infodeviceli} )
        else:
            return HttpResponse("enter correct details")
    else:
        infodevicefrm = infodevice_form()
        infodeviceli = infog.objects.filter(i_image__isnull = False)
        return render ( request , 'infodevice_add.html' , context = {'infodevicefrm' : infodevicefrm,'infodeviceli':infodeviceli} )


def infodevice_upd(request,id):
        infodeviceupd=infog.objects.get(id=id)
        infodevicefrm=infodevice_form(instance=infodeviceupd)
        if request.method=='POST':
            infodevicefrm=infodevice_form(request.POST,request.FILES, instance=infodeviceupd)
            print(infodevicefrm.errors)
            if infodevicefrm.is_valid():
                infodevicefrm.save()
                infodeviceli = infog.objects.filter(i_image__isnull = False)
                infodevicefrm =infodevice_form()
                messages.success(request,'data is updated')
                return render (request ,'infodevice_add.html' , context = {'infodevicefrm' : infodevicefrm,'infodeviceli':infodeviceli} )

            else:
                return HttpResponse("CORRECT YOUR DETAILS")
        else:
            infodevicefrm =infodevice_form(instance=infodeviceupd)
            infodeviceli = infog.objects.filter(i_image__isnull = False)
            return render ( request , 'infodevice_add.html' , context = {'infodevicefrm' : infodevicefrm,'infodeviceli':infodeviceli} )


def infodevice_del(request,id):
    infodevicedel=infog.objects.get(id=id)
    infodevicedel.delete()
    infodeviceli = infog.objects.filter(i_image__isnull = False)
    infodevicefrm =infodevice_form()
    messages.success(request,'data is deleted')
    return render ( request , 'infodevice_add.html' , context = {'infodevicefrm' : infodevicefrm,'infodeviceli':infodeviceli} )



def code_add(request):
    if request.method == 'POST':
        cdfrm = codes(request.POST)
        print(cdfrm)
        print(cdfrm.errors)
        cd = request.POST.get('cde')
        print(cd)
        print(type(cd))
        request.session['cd_code'] = cd
        print(request.session['cd_code'] )
        return redirect('infodatabase_add')
    else:
        cdfrm = codes()
        infodatabaseli = infog.objects.filter(image2field__isnull = False)
        return render (request , 'code.html' , context = {'cdfrm' : cdfrm , 'infodatabaseli' : infodatabaseli} )



def infodatabase_add(request):
    if request.method == "POST":
        infodatabasefrm = infodatabase_form(data=request.POST,filter_on=request.session['cd_code'])
        print(infodatabasefrm.errors)
        if infodatabasefrm.is_valid():
            try:
                infodatabasefrm.save()
            except:
                print('image is not there')
            infodatabaseli = infog.objects.filter (image2field__isnull = False)
            messages.success(request,'data is added')
            return render (request , 'infodatabase_add.html' , {'infodatabaseli' : infodatabaseli} )
        else:
            return HttpResponse("enter correct details")
    else:
        infodatabaseli = infog.objects.filter (image2field__isnull = False)
        infodatabasefrm = infodatabase_form ( filter_on = request.session.get('cd_code') )
        return render ( request , 'infodatabase_add.html' ,context = {'infodatabasefrm' : infodatabasefrm , 'infodatabaseli' : infodatabaseli} )





def codeupdate(request,id):
    if request.method == 'POST':
        cdfrm = codes(request.POST)
        print(cdfrm.errors)
        if cdfrm.is_valid:
            cd= request.POST.get('cde')
            print(cd)
            request.session['cd_code1'] = cd
            request.session['info_id'] = id
            print(request.session['cd_code1'])
            return redirect('infodatabase_upd')
        else:
            return HttpResponse("wrong data")
    else:
        infodatabaseli = infog.objects.filter(image2field__isnull = False)
        cdfrm = codes ()
        return render (request , 'code2.html' , context = {'cdfrm' : cdfrm , 'infodatabaseli' : infodatabaseli} )



def infodatabase_upd(request):
    if request.session['info_id'] == " ":
        infodatabasefrm = infodatabase_form (filter_on = request.session['cd_code1'])
        infodatabaseli = infog.objects.filter (image2field__isnull = False )
        return render ( request , 'infodatabase_add.html' , context={'infodatabasefrm' : infodatabasefrm,'infodatabaseli':infodatabaseli} )
    else:
        infodatabaseupd = infog.objects.get ( id = request.session['info_id'] )

        if request.method=='POST':

            infodatabasefrm=infodatabase_form(request.POST,filter_on=request.session['cd_code1'])
            print(infodatabasefrm.errors)
            if infodatabasefrm.is_valid():
                try:
                    infodatabasefrm.save()
                except:
                    pass
                infodatabaseli = infog.objects.filter (image2field__isnull = False)
                infodatabasefrm = infodatabase_form ( filter_on = request.session['cd_code1'] )
                messages.success(request,"data is updated")
                return render ( request , 'infodatabase_add.html' ,context = {'infodatabasefrm' : infodatabasefrm , 'infodatabaseli' : infodatabaseli} )
            else:
                return HttpResponse("CORRECT YOUR DETAILS")
        else:
            infodatabasefrm = infodatabase_form(instance=infodatabaseupd, filter_on = request.session['cd_code1'] )
            infodatabaseli = infog.objects.filter(image2field__isnull = False)
            return render ( request , 'infodatabase_add.html' , context = {'infodatabasefrm' : infodatabasefrm , 'infodatabaseli' : infodatabaseli} )


def infodatabase_del(request,id):
    infodatabasedel=infog.objects.get(id=id)
    infodatabasedel.delete()
    infodatabaseli = infog.objects.filter (image2field__isnull = False )
    infodatabasefrm = infodatabase_form(filter_on = request.session['cd_code'])
    messages.success(request,"data is deleted")
    return render(request , 'infodatabase_add.html' , context={'infodatabasefrm' : infodatabasefrm,'infodatabaseli':infodatabaseli})














