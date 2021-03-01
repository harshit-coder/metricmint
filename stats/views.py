
# Create your views here.
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from stats.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models import F
from stats.forms import *


def recent(request):
    request.session["searchtab"]= " "
    st=stat.objects.all().order_by('s_date')[:5]
    it=infog.objects.all().order_by('i_date')[:5]
    sfrm =searchform()
    return render(request,'homepage.html',context={'st':st,'it':it,'sfrm':sfrm})


def searchengine(request):
    if request.method == 'GET':
        se = request.GET.get('searc')
        request.session['searchtab'] = se
        print(se)
        sfrm = searchform ()
        si = stat.objects.filter(Q(s_subcategory__icontains = se) | Q(s_head_tittle__icontains = se) | Q(s_head_subtittle__icontains = se) | Q(graph_tittle__icontains = se) | Q(desc1__icontains = se ) | Q(s_date__icontains = se) | Q(x_axistittle__icontains = se) | Q(y_axistittle__icontains = se))
        ii = infog.objects.filter(Q(i_subcategory__icontains = se) | Q(i_head_tittle__icontains = se) | Q(i_sub_tittle__icontains = se) | Q(desc2__icontains = se) | Q(i_date__icontains = se) | Q(image_tittle__icontains = se))
        sef = searchenter(searc = se)
        sef.save()
        sfrm = searchform()
        return render(request,'searched.html', context={'se':request.session['searchtab'],'si':si,'ii':ii,'sfrm':sfrm})

def notfound(request):
    kl=request.session['searchtab']
    sfrm = searchform()
    return render(request,'notsearched.html',context={'kl':kl,'sfrm':sfrm})

def statpage(request,id):
    st = stat.objects.get(id= id)
    sfrm = searchform ()
    si= stat.objects.filter(s_head_tittle__icontains=request.session['searchtab'])[:10]
    return render(request,'stat.html',context={'st':st,'si':si ,'sfrm':sfrm})

def infopage(request,id):
    it = infog.objects.get(id= id)
    sfrm = searchform ()
    ii= infog.objects.filter(i_head_tittle__icontains=request.session['searchtab'])[:10]
    return render(request,'info.html',context={'it':it,'ii':ii,'sfrm':sfrm})

def about(request):
    sfrm = searchform ()
    return render(request,'aboutus.html',{'sfrm':sfrm})
