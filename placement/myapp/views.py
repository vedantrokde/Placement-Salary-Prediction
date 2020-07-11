from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
import numpy as np
import pickle as pickle
import joblib as joblib

path1 = './myapp/models/svc.pkl'
path2 = './myapp/models/rfr.pkl'

def home(requests):
    if requests.method=='GET':
        return render(requests,'index.html')
    else:
        name=requests.POST['name']
        gender=requests.POST['gender']
        secedper=requests.POST['secedper']
        hscper=requests.POST['hscper']
        hscspec=requests.POST['hscspec']
        degreeper=requests.POST['degreeper']
        typeofdeg=requests.POST['typeofdeg']
        workexp=requests.POST['workexp']
        weper=requests.POST['weper']
        
        model_list=[]

        if gender=='male':
            model_list.append(1)
        else :
            model_list.append(0)

        model_list.append(secedper)
        model_list.append(hscper)
        model_list.append(degreeper)

        if workexp=='yes':
            model_list.append(1)
        else:
            model_list.append(0)

        model_list.append(weper)

        if typeofdeg=='Sci&Tech':
          model_list.append(0)
          model_list.append(0)
          model_list.append(1)
        elif typeofdeg=='Comm&Mgmt':
          model_list.append(1)
          model_list.append(0)
          model_list.append(0)
        else:
          model_list.append(0)
          model_list.append(1)
          model_list.append(0)

        if hscspec=='Science':
          model_list.append(0)
          model_list.append(0)
          model_list.append(1)
        elif hscspec=='Commerce':
          model_list.append(1)
          model_list.append(0)
          model_list.append(0)
        else:
          model_list.append(0)
          model_list.append(1)
          model_list.append(0)

        model_array=np.array(model_list).reshape(1,-1)

        print(model_array)
    
        svc = joblib.load(path1)
        rfr = joblib.load(path2)
        placed = svc.predict(model_array)
        if int(placed[0])==0:
            salary = 0
        else :
            salary = rfr.predict(model_array)
            salary = salary[0]

        print(salary)
        print(placed)

        #if placed == 0 then display not placed and display salary as 0
        #if placed ==1 then display placed and display the salary

        if placed==1:
            placed='Placed'
        else:
            placed='Not Placed'

        params={'salary' : salary, 'placed':placed}

        return render(requests, 'result.html', params)
