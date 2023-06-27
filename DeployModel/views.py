from tkinter import Scale
from django.http import HttpResponse
from django.shortcuts import render 
import numpy as np
import pickle
import streamlit as st
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score







def home(request):
    return render(request,"diabetes.html")

def result(request):
    loaded_model = pickle.load(open("C:/Users/areeb/OneDrive/Desktop/Django/DeployModel-project/trained_model_Diabetes (1).sav",'rb'))
    
    
    lis=[]
    lis.append(request.GET['Pregnancies'])
    lis.append(request.GET['Glucose'])
    lis.append(request.GET['BloodPressure'])
    lis.append(request.GET['SkinThickness'])
    lis.append(request.GET['Insulin'])
    lis.append(request.GET['BMI'])
    lis.append(request.GET['DiabetesPredigreeFunction'])
    lis.append(request.GET['Age'])
    
    
# Change into numpy array

    
    input_data_as_numpy_array=np.asarray(lis)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    
    if (prediction[0]== 0):
        return render(request,"result.html",{'ans':'THE PERSON IS NOT DIABETIC'})
    else:
        return render(request,"result.html",{'ans':'THE PERSON IS DIABETIC'})
    



def home_two(request):
    return render(request,'heart.html')



def result_two(request):
    loaded_model_two = pickle.load(open("C:/Users/areeb/OneDrive/Desktop/Django/DeployModel-project/trained_model_Heart.sav",'rb'))
    
    
    list=[]
    list.append(request.GET['age'])
    list.append(request.GET['sex'])
    list.append(request.GET['cp'])
    list.append(request.GET['trestbps'])
    list.append(request.GET['chol'])
    list.append(request.GET['fbs'])
    list.append(request.GET['restecg'])
    list.append(request.GET['thalach'])
    list.append(request.GET['exang'])
    list.append(request.GET['oldpeak'])
    list.append(request.GET['slope'])
    list.append(request.GET['ca'])
    list.append(request.GET['thal'])
    

 
 
# Change into numpy array

    
    input_data_as_numpy_array=np.asarray(list)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model_two.predict(input_data_reshaped)
    
    if (prediction[0]== 0):
        return render(request,"result_two.html",{'ans':'THE PERSON IS NOT HAVING HEART PROBLEMS'})
    else:
        return render(request,"result_two.html",{'ans':'THE PERSON IS HAVING HEART PROBLEMS '})
    
    
    
      
    
def feedbackForm(request):
    return render(request,'feedbackForm.html')

def rating(request):
    return render(request,'rating.html')

def remediesD(request):
    return render(request,'remediesD.html')

def remediesH(request):
    return render(request,'remediesH.html')

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def appointmentH(request):
    return render(request,'appointmentH.html')

def appointmentD(request):
    return render(request,'appointmentD.html')

def bmi_calculator(request):
    if request.method == 'POST':
        weight = float(request.POST.get('weight'))
        height = float(request.POST.get('height'))
        bmi = weight / (height ** 2)
        return render(request, 'bmi.html', {'bmi': bmi})
    else:
        return render(request, 'bmi_form.html')

def yoga(request):
    return render(request,'yoga.html')

def diet(request):
    return render(request,'diet.html')





def resultLungs(request):
    loaded_model_two = pickle.load(open("C:/Users/areeb/OneDrive/Desktop/Django/DeployModel-project/trained_model_Lungs (2).sav",'rb'))
    
    
    list=[]
    list.append(request.GET['Gender'])
    list.append(request.GET['Age'])
    list.append(request.GET['Smoking'])
    list.append(request.GET['Yellow fingers'])
    list.append(request.GET['Anxiety'])
    list.append(request.GET['Peer_pressure'])
    list.append(request.GET['Chronic_Disease'])
    list.append(request.GET['Fatigue'])
    list.append(request.GET['Allergy'])
    list.append(request.GET['Wheezing'])
    list.append(request.GET['Alcohol'])
    list.append(request.GET['Coughing'])
    list.append(request.GET['Shortness of Breath'])
    list.append(request.GET['Swallowing Difficulty'])
    list.append(request.GET['Chest Pain'])
    
    

 
 
# Change into numpy array

    
    input_data_as_numpy_array=np.asarray(list)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model_two.predict(input_data_reshaped)
    
    if (prediction[0]== 0):
        return render(request,"resultLungs.html",{'ans':'THE PERSON IS NOT HAVING LUNGS PROBLEMS'})
    else:
        return render(request,"resultLungs.html",{'ans':'THE PERSON IS HAVING LUNGS PROBLEMS '})


    
def lungs(request):
    return render(request,'lungs.html')

def Kidney(request):
    return render(request,'Kidney.html')

def resultKidney(request):
    loaded_model_two = pickle.load(open("C:/Users/areeb/OneDrive/Desktop/Django/DeployModel-project/trained_model_kidney (2).sav",'rb'))
    
    
    list=[]
    list.append(request.GET['Age'])
    list.append(request.GET['Blood Pressure'])
    list.append(request.GET['Specific Gravity'])
    list.append(request.GET['Albumin'])
    list.append(request.GET['Sugar'])
    list.append(request.GET['Red Blood Cells'])
    list.append(request.GET['Pus Cell'])
    list.append(request.GET['Pus Cell Clumps'])
    list.append(request.GET['Bacteria'])
    list.append(request.GET['Blood Glucose Random'])
    list.append(request.GET['Blood Urea'])
    list.append(request.GET['Serum Creatinine'])
    list.append(request.GET['Sodium'])
    list.append(request.GET['Potassium'])
    list.append(request.GET['Hemoglobin'])
    list.append(request.GET['Packed Cell Volume'])
    list.append(request.GET['White Blood Cell Count'])
    list.append(request.GET['Red Blood Cell Count'])
    list.append(request.GET['Hypertension'])
    list.append(request.GET['Diabetes Mellitus'])
    list.append(request.GET['Coronary Artery Disease'])
    list.append(request.GET['Appetite'])
    list.append(request.GET['Pedal Edema'])
    list.append(request.GET['Anemia'])
    
    

 
 
# Change into numpy array

    
    input_data_as_numpy_array=np.asarray(list)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model_two.predict(input_data_reshaped)
    
    if (prediction[0]== 0):
        return render(request,"resultKidney.html",{'ans':'THE PERSON IS NOT HAVING KIDNEY PROBLEMS'})
    else:
        return render(request,"resultKidney.html",{'ans':'THE PERSON IS HAVING KIDNEY PROBLEMS '})

