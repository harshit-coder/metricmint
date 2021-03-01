

#def search1(request):
 #   se = request.GET['searches']
  #  co=request.GET['c_ountry']
  #  ca= request.GET['c_ategory']


   # request.session['searchtab']=se
 #   if pa == "stat":
      #  if co =="ALL" and ca =="ALL":
      #      si = stat.objects.filter(Q(s_category__icontains = request.session['searchtab'])|Q(s_subcategory__icontains = request.session['searchtab'])|Q(s_head_tittle__icontains = request.session['searchtab'])|Q(s_head_subtittle__icontains = request.session['searchtab'])|Q(graph_tittle__icontains = request.session['searchtab'])|Q(graph_result__icontains = request.session['searchtab'])|Q(desc1__icontains = request.session['searchtab'])|Q(desc2__icontains = request.session['searchtab'])|Q(desc3__icontains = request.session['searchtab'])|Q(s_count__icontains = request.session['searchtab'])|Q(s_date__icontains = request.session['searchtab']))
      #      if len(si) == 0 :
           #     return redirect('notfound')
        #    else :
              #  return render(request,'searched.html',context={'ss':request.session['searchtab'],'si':si})

     #   elif  co == "ALL"  and  ca !=  "ALL" :
         #   si = stat.objects.filter(Q(Q(s_subcategory__icontains = request.session['searchtab'])|Q(s_head_tittle__icontains = request.session['searchtab'])|Q(s_head_subtittle__icontains = request.session['searchtab'])|Q(graph_tittle__icontains = request.session['searchtab'])|Q(graph_result__icontains = request.session['searchtab'])|Q(desc1__icontains = request.session['searchtab'])|Q(desc2__icontains = request.session['searchtab'])|Q(desc3__icontains = request.session['searchtab'])|Q(s_count__icontains = request.session['searchtab'])|Q(s_date__icontains = request.session['searchtab']))&(Q(s_category = ca)))
           # if len(si) == 0:
         #       return redirect('notfound')
          #  else :
            #    return render(request,'searched.html',context={'ss':request.session['searchtab'],'si':si})

       # elif co != "ALL" and ca == "ALL":
         #   si = stat.objects.filter(Q(Q(Q(s_category__icontains = request.session['searchtab'])|Q(s_subcategory__icontains = request.session['searchtab'])|Q(s_head_tittle__icontains = request.session['searchtab'])|Q(s_head_subtittle__icontains = request.session['searchtab'])|Q(graph_tittle__icontains = request.session['searchtab'])|Q(graph_result__icontains = request.session['searchtab'])|Q(desc1__icontains = request.session['searchtab'])|Q(desc2__icontains = request.session['searchtab'])|Q(desc3__icontains = request.session['searchtab'])|Q(s_date__icontains = request.session['searchtab']))&Q(s_count = co))
         #   if len(si) == 0:
            #    return redirect('notfound')
          #  else :
            #    return render(request,'searched.html',context={'ss':request.session['searchtab'],'si':si})
        
      #  else :
         #   si = stat.objects.filter(Q(Q(Q(s_subcategory__icontains = request.session['searchtab'])|Q(s_head_tittle__icontains = request.session['searchtab'])|Q(s_head_subtittle__icontains = request.session['searchtab'])|Q(graph_tittle__icontains = request.session['searchtab'])|Q(graph_result__icontains = request.session['searchtab'])|Q(desc1__icontains = request.session['searchtab'])|Q(desc2__icontains = request.session['searchtab'])|Q(desc3__icontains = request.session['searchtab'])|Q(s_date__icontains = request.session['searchtab']))&Q(s_category = ca)&Q(s_count = co))
          #  if len(si) == 0:
          #      return redirect('notfound')
          #  else :
          #      return render(request,'searched.html',context={'ss':request.session['searchtab'],'si':si})


   # elif pa == "infog":
      #  if co =="ALL" and ca =="ALL":
        #    ii = infog.objects.filter(Q(i_category__icontains = request.session['searchtab'])|Q(i_subcategory__icontains = request.session['searchtab'])|Q(i_head_tittle__icontains = request.session['searchtab'])|Q(i_sub_tittle__icontains = request.session['searchtab'])|Q(i_desc__icontains = request.session['searchtab'])|Q(i_count__icontains = request.session['searchtab'])|Q(i_date__icontains = request.session['searchtab']))
         #   if len(ii) == 0:
            #    return redirect('notfound')
          #  else :
              #  return render(request,'searched.html',context={'ss':request.session['searchtab'],'ii':ii})
        
     #   elif co =="ALL" and ca != "ALL":
        #    ii = infog.objects.filter(Q(Q(i_subcategory__icontains = request.session['searchtab'])|Q(i_head_tittle__icontains = request.session['searchtab'])|Q(i_sub_tittle__icontains = request.session['searchtab'])|Q(i_desc__icontains = request.session['searchtab'])|Q(i_count__icontains = request.session['searchtab'])|Q(i_date__icontains = request.session['searchtab']))&Q(i_category = ca))
        #    if len(ii) == 0:
         #       return redirect('notfound')
        #    else :
          #      return render(request,'searched.html',context={'ss':request.session['searchtab'],'ii':ii})
        
  #      elif co != "ALL" and ca == "ALL":
      #      ii = infog.objects.filter(Q(Q(i_category__icontains = request.session['searchtab'])|Q(i_subcategory__icontains = request.session['searchtab'])|Q(i_head_tittle__icontains = request.session['searchtab'])|Q(i_sub_tittle__icontains = request.session['searchtab'])|Q(i_desc__icontains = request.session['searchtab'])|Q(i_date__icontains = request.session['searchtab']))&Q(i_count = co))
         #   if len(ii) == 0:
      #          return redirect('notfound')
        #    else :
         #       return render(request,'searched.html',context={'ss':request.session['searchtab'],'ii':ii})
        
      #  else :
         #   ii = infog.objects.filter(Q(Q(i_subcategory__icontains = request.session['searchtab'])|Q(i_head_tittle__icontains = request.session['searchtab'])|Q(i_sub_tittle__icontains = request.session['searchtab'])|Q(i_desc__icontains = request.session['searchtab'])|Q(i_date__icontains = request.session['searchtab']))&Q(i_category = ca)&Q(i_count = co))
       #     if len(ii) == 0:
         #       return redirect('notfound')
        #    else :
          #      return render(request,'searched.html',context={'ss':request.session['searchtab'],'ii':ii})
        

  #  elif pa == "reports":
    #    if co =="ALL" and ca =="ALL":
       #     ri = reports.objects.filter(Q(Q(r_category__icontains = request.session['searchtab'])|Q(r_subcategory__icontains = request.session['searchtab'])|Q(r_tittle__icontains = request.session['searchtab'])|Q(r_subtittle__icontains = request.session['searchtab'])|Q(r_desc__icontains = request.session['searchtab'])|Q(desc1__icontains = request.session['searchtab'])|Q(r_count__icontains = request.session['searchtab'])|Q(r_date__icontains = request.session['searchtab']))
        #    if len(ri) == 0:
           #     return redirect('notfound')
        #    else :
          #      return render(request,'searched.html',context={'ss':request.session['searchtab'],'ri':ri})
      #  elif co =="ALL" and ca != "ALL":
        #    ri = reports.objects.filter(Q(Q(Q(r_subcategory__icontains = request.session['searchtab'])|Q(r_tittle__icontains = request.session['searchtab'])|Q(r_subtittle__icontains = request.session['searchtab'])|Q(r_desc__icontains = request.session['searchtab'])|Q(desc1__icontains = request.session['searchtab'])|Q(r_count__icontains = request.session['searchtab'])|Q(r_date__icontains = request.session['searchtab']))&Q(r_category = ca))
         #   if len(ri) == 0:
        #        return redirect('notfound')
           # else :
              #  return render(request,'searched.html',context={'ss':request.session['searchtab'],'ri':ri})
        
      #  elif co != "ALL" and ca == "ALL":
         #   ri = reports.objects.filter(Q(Q(Q(r_category__icontains = request.session['searchtab'])|Q(r_subcategory__icontains = request.session['searchtab'])|Q(r_tittle__icontains = request.session['searchtab'])|Q(r_subtittle__icontains = request.session['searchtab'])|Q(r_desc__icontains = request.session['searchtab'])|Q(desc1__icontains = request.session['searchtab'])|Q(r_date__icontains = request.session['searchtab']))&Q(r_count = co))
         #   if len(ri) == 0:
          #      return redirect('notfound')
          #  else :
           #     return render(request,'searched.html',context={'ss':request.session['searchtab'],'ri':ri})
        
     #   else :
         #   ri = reports.objects.filter(Q(Q(Q(r_subcategory__icontains = request.session['searchtab'])|Q(r_tittle__icontains = request.session['searchtab'])|Q(r_subtittle__icontains = request.session['searchtab'])|Q(r_desc__icontains = request.session['searchtab'])|Q(desc1__icontains = request.session['searchtab'])|Q(r_date__icontains = request.session['searchtab']))&Q(r_category = ca)&Q(r_count = co))
         #   if len(ri) == 0:
         #       return redirect('notfound')
         #   else :
            #    return render(request,'searched.html',context={'ss':request.session['searchtab'],'ri':ri})


   # else :
      #  if co =="ALL" and ca =="ALL":
         #   si = stat.objects.filter(Q(Q(s_category__icontains = request.session['searchtab'])|Q(s_subcategory__icontains = request.session['searchtab'])|Q(s_head_tittle__icontains = request.session['searchtab'])|Q(s_head_subtittle__icontains = request.session['searchtab'])|Q(graph_tittle__icontains = request.session['searchtab'])|Q(graph_result__icontains = request.session['searchtab'])|Q(desc1__icontains = request.session['searchtab'])|Q(desc2__icontains = request.session['searchtab'])|Q(desc3__icontains = request.session['searchtab'])|Q(s_count__icontains = request.session['searchtab'])|Q(s_date__icontains = request.session['searchtab']))
          #  ii = infog.objects.filter(Q(i_category__icontains = request.session['searchtab'])|Q(i_subcategory__icontains = request.session['searchtab'])|Q(i_head_tittle__icontains = request.session['searchtab'])|Q(i_sub_tittle__icontains = request.session['searchtab'])|Q(i_desc__icontains = request.session['searchtab'])|Q(i_count__icontains = request.session['searchtab'])|Q(i_date__icontains = request.session['searchtab']))
           # ri = reports.objects.filter(Q(Q(r_category__icontains = request.session['searchtab'])|Q(r_subcategory__icontains = request.session['searchtab'])|Q(r_tittle__icontains = request.session['searchtab'])|Q(r_subtittle__icontains = request.session['searchtab'])|Q(r_desc__icontains = request.session['searchtab'])|Q(desc1__icontains = request.session['searchtab'])|Q(r_count__icontains = request.session['searchtab'])|Q(r_date__icontains = request.session['searchtab']))
           # if len(si) == 0 and len(ii) == 0 and len(ri) == 0 :
           #     return redirect('notfound')
           # else:
             #   return render(request,'searched.html', context={'ss':request.session['searchtab'],'si':si,'ii':ii,'ri':ri})

       # elif co =="ALL" and ca != "ALL":
         #   si = stat.objects.filter(Q(Q(Q(s_subcategory__icontains = request.session['searchtab'])|Q(s_head_tittle__icontains = request.session['searchtab'])|Q(s_head_subtittle__icontains = request.session['searchtab'])|Q(graph_tittle__icontains = request.session['searchtab'])|Q(graph_result__icontains = request.session['searchtab'])|Q(desc1__icontains = request.session['searchtab'])|Q(desc2__icontains = request.session['searchtab'])|Q(desc3__icontains = request.session['searchtab'])|Q(s_count__icontains = request.session['searchtab'])|Q(s_date__icontains = request.session['searchtab']))&Q(s_category = ca))
         #   ii = infog.objects.filter(Q(Q(i_subcategory__icontains = request.session['searchtab'])|Q(i_head_tittle__icontains = request.session['searchtab'])|Q(i_sub_tittle__icontains = request.session['searchtab'])|Q(i_desc__icontains = request.session['searchtab'])|Q(i_count__icontains = request.session['searchtab'])|Q(i_date__icontains = request.session['searchtab']))&Q(i_category = ca))
         #   ri = reports.objects.filter(Q(Q(Q(r_subcategory__icontains = request.session['searchtab'])|Q(r_tittle__icontains = request.session['searchtab'])|Q(r_subtittle__icontains = request.session['searchtab'])|Q(r_desc__icontains = request.session['searchtab'])|Q(desc1__icontains = request.session['searchtab'])|Q(r_count__icontains = request.session['searchtab'])|Q(r_date__icontains = request.session['searchtab']))&Q(r_category = ca))
          #  if len(si) == 0 and len(ii) == 0 and len(ri) == 0 :
           #     return redirect('notfound')
          #  else:
            #    return render(request,'searched.html', context={'ss':request.session['searchtab'],'si':si,'ii':ii,'ri':ri})

      #  elif co != "ALL" and ca == "ALL":
          #  si = stat.objects.filter(Q(Q(Q(s_category__icontains = request.session['searchtab'])|Q(s_subcategory__icontains = request.session['searchtab'])|Q(s_head_tittle__icontains = request.session['searchtab'])|Q(s_head_subtittle__icontains = request.session['searchtab'])|Q(graph_tittle__icontains = request.session['searchtab'])|Q(graph_result__icontains = request.session['searchtab'])|Q(desc1__icontains = request.session['searchtab'])|Q(desc2__icontains = request.session['searchtab'])|Q(desc3__icontains = request.session['searchtab'])|Q(s_date__icontains = request.session['searchtab']))&Q(s_count = co))
          #  ii = infog.objects.filter(Q(Q(i_category__icontains = request.session['searchtab'])|Q(i_subcategory__icontains = request.session['searchtab'])|Q(i_head_tittle__icontains = request.session['searchtab'])|Q(i_sub_tittle__icontains = request.session['searchtab'])|Q(i_desc__icontains = request.session['searchtab'])|Q(i_date__icontains = request.session['searchtab']))&Q(i_count = co))
          #  ri = reports.objects.filter(Q(Q(Q(r_category__icontains = request.session['searchtab'])|Q(r_subcategory__icontains = request.session['searchtab'])|Q(r_tittle__icontains = request.session['searchtab'])|Q(r_subtittle__icontains = request.session['searchtab'])|Q(r_desc__icontains = request.session['searchtab'])|Q(desc1__icontains = request.session['searchtab'])|Q(r_date__icontains = request.session['searchtab']))&Q(r_count = co))
           # if len(si) == 0 and len(ii) == 0 and len(ri) == 0 :
           #     return redirect('notfound')
        #   else:
         #       return render(request,'searched.html', context={'ss':request.session['searchtab'],'si':si,'ii':ii,'ri':ri})

    #    else :
    #        si = stat.objects.filter(Q(Q(Q(s_subcategory__icontains = request.session['searchtab'])|Q(s_head_tittle__icontains = request.session['searchtab'])|Q(s_head_subtittle__icontains = request.session['searchtab'])|Q(graph_tittle__icontains = request.session['searchtab'])|Q(graph_result__icontains = request.session['searchtab'])|Q(desc1__icontains = request.session['searchtab'])|Q(desc2__icontains = request.session['searchtab'])|Q(desc3__icontains = request.session['searchtab'])|Q(s_date__icontains = request.session['searchtab']))&Q(s_category = ca)&Q(s_count = co))
       #     ii = infog.objects.filter(Q(Q(i_subcategory__icontains = request.session['searchtab'])|Q(i_head_tittle__icontains = request.session['searchtab'])|Q(i_sub_tittle__icontains = request.session['searchtab'])|Q(i_desc__icontains = request.session['searchtab'])|Q(i_date__icontains = request.session['searchtab']))&Q(i_category = ca)&Q(i_count = co))
        #    ri = reports.objects.filter(Q(Q(Q(r_subcategory__icontains = request.session['searchtab'])|Q(r_tittle__icontains = request.session['searchtab'])|Q(r_subtittle__icontains = request.session['searchtab'])|Q(r_desc__icontains = request.session['searchtab'])|Q(desc1__icontains = request.session['searchtab'])|Q(r_date__icontains = request.session['searchtab']))&Q(r_category = ca)&Q(r_count = co))
         #   if len(si) == 0 and len(ii) == 0 and len(ri) == 0 :
            #    return redirect('notfound')
          #  else:
         #       return render(request,'searched.html', context={'ss':request.session['searchtab'],'si':si,'ii':ii,'ri':ri})

