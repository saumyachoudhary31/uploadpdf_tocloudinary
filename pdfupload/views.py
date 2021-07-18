
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
#from .serializers import FileSerializer
import cloudinary.uploader
#from .models import KeyVal,Dicty
#from . models import File,Data
from .models import Entry,Author
from .serializers import EntrySerializer
#from .forms import PDFUPLOADForms
from django.http import HttpResponse
from .serializers import YourSerializer
#from .serializers import PortfolioSerializer
import tabula
from tabula import read_pdf
import camelot
import pandas as pd
import numpy as np
import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["second"]
company= db["abc"]


cloudinary.config( 
  cloud_name = "dg3tuf3qk", 
  api_key = "323617195866446", 
  api_secret = "6yb3yhWlcDrphTuS5wFHEm10jwU" 
)
from rest_framework import viewsets
class EntryViewSet(viewsets.ModelViewSet):
    """entry api endpoint"""
    queryset = Entry.objects.all().order_by('-id')
    serializer_class = EntrySerializer

# class newviewsete(viewsets.ModelViewSet):
#    queryset = Entry.objects.all().order_by('-id')
#    serializer_class = PortfolioSerializer

from django.http import HttpResponse
    
def xyz(request):
   if request.method == 'POST' and request.FILES['myfile']:
        print(request.FILES)
        d=dict(request.FILES)
        print(d)
        print(type(d))
  
        for i in d:
          print("this is output of request.data.i ")
          print(d[i])
          for j in d[i]:
            print(j)
        print(type(request.FILES['myfile']))
        # response=cloudinary.uploader.upload(request.FILES['myfile'],resource_type = "raw")
        # ur=dump_response(response)
        # print("ur="+ur)
        # tables = camelot.read_pdf(ur)
        # print(tables)
        # tables[0]
        # final = tables[0].df
        # final
        # final.drop(1,axis=1,inplace=True)
        # final1 = final.rename(columns={0: 'Date'})
        # final1 = final1.replace(r'\n',' ', regex=True)
        # final2 = final1.rename(columns={2: 'Description'})
        # final3 = final2.rename(columns={3: 'Ref no'})
        # final4 = final3.rename(columns={4: 'Debit'})
        # final5 = final4.rename(columns={5: 'Credit'})
        # finaln = final5.rename(columns={6: 'Balance'})
        # finaln.drop(0,axis=0,inplace=True)
        # df = pd.DataFrame(finaln)
        # df["Balance"]= df["Balance"].str.replace('[\,]', '').astype(float)
        # t=(df.replace(r'^\s*$', np.nan, regex=True))
        # t['Credit'] = t['Credit'].fillna(0)
        # t['Debit'] = t['Debit'].fillna(0)
        # t["Credit"]= t["Credit"].str.replace('[\,]', '').astype(float)
        # t["Debit"]= t["Debit"].str.replace('[\,]', '').astype(float)
        # t = t.replace(r'\n',' ', regex=True)
        # t=t.assign(cat="")
        # t

        # pd.set_option('display.max_columns',None)

        # pd.set_option('max_colwidth',None)

        # r=pd.concat([t['Date'],t['Description'],t['Debit'],t['Credit']],axis=1)
        # r['Credit'] = r['Credit'].fillna(0)
        # r['Debit'] = r['Debit'].fillna(0)
        # print(r)
        # data_dict = r.to_dict("records")
        # print(data_dict)

        # company.insert_one({"index":"date","data":data_dict,"url":ur})
        # html_table = r.to_html(index=False)
        # return render(request, 'html_table.html', {
        #     'html_table': html_table
        # })
        return HttpResponse("ok")
        
   return render(request,"home.html")
# def new(request):
#   rfor=Dicty()
#   rfor.name="ijkl"
#   rfor.save()
#   kfor=KeyVal()
#   kfor.key="abcd"
#   kfor.value="efgh"
#   kfor.container=rfor
#   kfor.save()
#   print(kfor)
  # return HttpResponse("yes")
def newone(request):
  newauther= Author()
  # newautherxyz=Author()


    
  # newauther.name="cnjdakl123"
  # newauther.email="ana@fgmail.com"
  
  # newautherxyz.name="addd123"



  # newautherxyz.email="f@m.com"
  # print(newauther.name)
  # print(newauther.email)
  #newauther={'name': 'John', 'email': 'john@mail.com'},

  
  entry = Entry()
  # some=[{'name': 'John', 'email': 'john@mail.com'},
  #              {'name': 'Paul', 'email': 'paul@mail.com'}]
  # name_list = []

  # for d in some :
  #   for i in d['name']:
  #     name_list.append(i)              
  # print (name_list)
#  for i in range(2):

#    locals()["newauthor{0}".format(i)]= Author()
   




  # count=0
  # for iin in some:
  #   for i in range(2):
  #     print(count)
  #     for kiin in iin:
  #       print (type(kiin))
  #       print ('kkin', kiin)
  #       count=Author()
  #       #count.name=iin[kiin]
  #       # print(count.name)
        
  #       # count.email=iin[kiin]
  #       # print(count.email)
  #       if kiin=="name":
  #         count.name=iin[kiin]
          
          
  #       if kiin=="email":
  #         count.email=iin[kiin]
  #       somelist.append(count)
  #       print(somelist)

  # for something in somelist:
  #   print(something)
    

  entry.headline="hfoenow123"
  entry.authors=[newauther]
  entry.save()
  # datafor=Data()
  # filefor=File()
  # datafor.Date="today"
  # datafor.Description="fg"
  # datafor.Debit=3.0
  # datafor.Credit=4.0
  # datafor.save()
  # filefor.UR="jkk"
  # filefor.DataSaved=datafor
  # filefor.save()
  return HttpResponse("ok")





def dump_response(response):
    print("Upload response:")
    for key in sorted(response.keys()):
        print("  %s: %s" % (key, response[key]))
        if key=='url':
            uploadedurl=response[key]
            return(uploadedurl)

class FileView(APIView):
  parser_classes = (MultiPartParser, FormParser)
  def post(self, request, *args, **kwargs):
    print(request.data)
    print(type(request.data))
    d=dict(request.data)
    print(d)
    print(type(d))
    ur=""
    bankname=d.get('BankName')
    for i in d:
      print("this is output of request.data.i ")
      print(d[i])
      if i=='file':
        for j in d[i]:
          print(j)
          response=cloudinary.uploader.upload(j,resource_type = "raw")
          print("this is output of response")
          print(response)
          for key in sorted(response.keys()):
            print("  %s: %s" % (key, response[key]))
            if key=='url':
              ur=response[key]
          df2 = read_pdf(ur, pages='all', encoding='utf-8', lattice=False, multiple_tables=True)
          print(df2)
          ds=pd.DataFrame([])
          ds=ds.append(df2)
          print(ds)
          if bankname=='SBI':
            ds.drop(['Value\rDate'], axis=1,inplace=True)
            
            ds.rename(columns={'Txn Date': 'TxnDate'},inplace=True)
            ds.rename(columns={' Description': 'Description'},inplace=True)
            ds.rename(columns={'Ref No./Cheque\rNo.': 'Chequenumber'},inplace=True)
            ds.drop(['Chequenumber'], axis=1,inplace=True)
            ds.rename(columns={'Debit': 'Debit'},inplace=True)
            ds.rename(columns={'Credit': 'Credit'},inplace=True)
            ds.rename(columns={'Balance': 'Balance'},inplace=True)
          elif bankname=='Axis':
            ds=ds.rename(columns={'Init.':'Init'})
            ds.drop(['Init'], axis=1,inplace=True)
            ds.drop(['Unnamed: 0'], axis=1,inplace=True)
            ds.rename(columns={'Tran Date': 'TxnDate'},inplace=True)
            ds.rename(columns={'Chq No Particulars': 'Description'},inplace=True)
      
            ds.rename(columns={'Debit': 'Debit'},inplace=True)
            ds.rename(columns={'Credit': 'Credit'},inplace=True)
            ds.rename(columns={'Balance': 'Balance'},inplace=True)
          print(ds)
          data_dict = ds.to_dict("records")
          company.insert_one({"index":"date","data":data_dict,"url":ur,"bankname":bankname})
          yourdata= data_dict
          results = YourSerializer(yourdata, many=True).data
        
            
    return Response(status=status.HTTP_201_CREATED,)
    # tables = camelot.read_pdf(ur)
    # print(tables)
    # tables[0]
    # final = tables[0].df
    # final
    # final.drop(1,axis=1,inplace=True)
    # final1 = final.rename(columns={0: 'Date'})
    # final1 = final1.replace(r'\n',' ', regex=True)
    # final2 = final1.rename(columns={2: 'Description'})
    # final3 = final2.rename(columns={3: 'Ref no'})
    # final4 = final3.rename(columns={4: 'Debit'})
    # final5 = final4.rename(columns={5: 'Credit'})
    # finaln = final5.rename(columns={6: 'Balance'})
    # finaln.drop(0,axis=0,inplace=True)
    # df = pd.DataFrame(finaln)
    # df["Balance"]= df["Balance"].str.replace('[\,]', '').astype(float)
    # t=(df.replace(r'^\s*$', np.nan, regex=True))
    # t['Credit'] = t['Credit'].fillna(0)
    # t['Debit'] = t['Debit'].fillna(0)
    # t["Credit"]= t["Credit"].str.replace('[\,]', '').astype(float)
    # t["Debit"]= t["Debit"].str.replace('[\,]', '').astype(float)
    # t = t.replace(r'\n',' ', regex=True)
    # t=t.assign(cat="")
    # t

    # pd.set_option('display.max_columns',None)

    # pd.set_option('max_colwidth',None)

    # r=pd.concat([t['Date'],t['Description'],t['Debit'],t['Credit']],axis=1)

    # r['Credit'] = r['Credit'].fillna(0)
    # r['Debit'] = r['Debit'].fillna(0)
    # print(r)
    # data_dict = r.to_dict("records")
    # company.insert_one({"index":"date","data":data_dict,"url":ur})
    # yourdata= data_dict
    # results = YourSerializer(yourdata, many=True).data
    # return Response(results ,status=status.HTTP_201_CREATED,)
    
    # file_serializer = FileSerializer(data=request.data)
    # print("               request.data   ")
    # print(request.data)
    
    # if file_serializer.is_valid():
    #    file_serializer.save(UR=ur)
    #    return Response(file_serializer.data,status=status.HTTP_201_CREATED,)
    # else:
    #    return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
