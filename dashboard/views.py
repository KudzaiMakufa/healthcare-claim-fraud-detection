from django.shortcuts import render
import calendar
from datetime import datetime
from django.contrib.auth.decorators import login_required , permission_required
from django.urls.base import translate_url
from requests.api import head
from pypi_simple import PyPISimple 
from dashboard.forms import Library_Form 
from dashboard.models import  Library, Physician, Provider , Beneficiary
from django.contrib import messages
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect
import vulners  
from django.core.mail import send_mail
import random
import pandas as pd
import requests
import json
from io import StringIO
import base64

from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
from time import sleep
from medclaim.settings import MEDIA_ROOT



@login_required
def dashboard_index(request):
    form = None
    url = "dashboard/index.html" 
    if request.method == 'POST':
        form = Library_Form(request.POST, request.FILES)
        if(form.is_valid()):
            data = form.save(commit=False)
        
            
            data.created_at = timezone.now()
            data.updated_at = timezone.now()
            data.created_by = request.user.id   
            data.save()
            messages.add_message(request, messages.INFO, 'File saved')
            return HttpResponseRedirect(reverse('dashboard:libraries'))
     
    else:
        form = Library_Form()
    
    context = {
         
        'title': "Claim submission portal",
        'form':form
        
    } 
     
    return render(request , url , context)






def dashboard_libraries(request):
    libraries = Library.objects.all().order_by('-id')
    url = "dashboard/list_librabries.html" 
 
    context = {
        
        'title': "Listing claims",
        'libraries':libraries
        
    } 


    return render(request , url , context)


@login_required
def delete_claim(request ,librabry_id=None):
    library = Library.objects.get(pk=librabry_id)
    library.delete()
    messages.add_message(request, messages.INFO, 'Library deleted')
    return HttpResponseRedirect('/dashboard/libraries')


def upload_data(request):

    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        import pandas as pd

        df = pd.read_csv(MEDIA_ROOT+"/uploads/Train_Inpatientdata-1542865627584.csv")


        for index, row in df.iterrows():

           
            data = {}
            data['physician_id'] = row['OperatingPhysician']
            # data['potential_fraud'] = row['PotentialFraud']

            # data['nationality'] = row['replace']
            # data['allergies'] = row['replace']
            # data['medical_aid_scheme'] = row['replace']
            # data['medical_aid_number'] = row['replace']
            # data['next_of_kin_name'] = row['replace']
            # data['next_of_kin_phone_number'] = row['replace']
           

            provider = Physician.objects.create(**data)
            provider.save()
            print(data)
            print("_______________________________________________")
    context = {
        
        'title': "Data upload" ,
    }

    return render(request, 'dashboard/list_librabries.html', context)
