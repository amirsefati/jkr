from django.shortcuts import render
from django.http import HttpResponse
import os
from bs4 import BeautifulSoup
import requests
from getdata.models import Archive

# Create your views here.

all_id = []
not_in_search = []

def getfile(request):
    now_dir = os.path.dirname(__file__)
    file_path = os.path.join(now_dir,'MarketWatch.htm')
    soup = BeautifulSoup(open(file_path,encoding="utf8"),"html.parser")

    class_tag = soup.findAll(class_="{c}")

    for i in class_tag:
        all_id.append(i.get('id'))

    all_archive_ids = []
    all_archive = Archive.objects.all()
    for id_in_archive in all_archive:
        all_archive_ids.append(id_in_archive.Ta1)

    for tbl1 in all_id:
        
        if(tbl1 not in all_archive_ids):

            shenase = requests.get("http://www.tsetmc.ir/Loader.aspx?Partree=15131M&i={}".format(tbl1))
            shenase_all = BeautifulSoup(shenase.text,'html.parser')
            table = shenase_all.findAll('table',{"class","table1"})

            shenase_in_loop = []

            for tr in table:
                rows = tr.findAll('td')
                for td in rows:
                    if(rows.index(td) % 2 != 0):
                        shenase_in_loop.append(td.get_text())

            name = shenase_in_loop[5]
            name = name.split(' ', 1)[0]

            search = requests.get('http://www.tsetmc.com/tsev2/data/search.aspx?skey={}'.format(name))
            search_arr = search.text.split(",")
            if(len(str(search_arr)) > 20):
                if( name in search_arr):
                    tbl = search_arr.index(name)

                save_shenasname = Archive(Ta1=tbl1,C12Na=shenase_in_loop[0],C5Na=shenase_in_loop[1],
                    NLSh=shenase_in_loop[2],C4Sh=shenase_in_loop[3],NSh=shenase_in_loop[4],NaF=shenase_in_loop[5],
                    Na30F=shenase_in_loop[6],C12Sh=shenase_in_loop[7],B=shenase_in_loop[8],CTa=shenase_in_loop[9],
                    CGI=shenase_in_loop[10],GI=shenase_in_loop[11],CSGI=shenase_in_loop[12],SGI=shenase_in_loop[13],
                    Ta2=search_arr[tbl + 3],Ta3=search_arr[tbl + 4],Ta4=search_arr[tbl + 5])
                save_shenasname.save()
            else:
                not_in_search.append({})
                
            return HttpResponse(not_in_search)

