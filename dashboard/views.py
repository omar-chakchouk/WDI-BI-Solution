from django.shortcuts import render
import imaplib
import pandas as pd
from sklearn.linear_model import LinearRegression
from django.shortcuts import render, get_object_or_404
import imaplib
from django.shortcuts import render
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from email.header import decode_header
import numpy as np
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
import joblib
import pandas as pd
from django.shortcuts import render
from sklearn import tree
from django.shortcuts import render
import pickle
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder








def index(request):
    return render(request, 'index.html')






def chart(request):
   
     if request.method == 'POST':
        # Retrieve the input values from the form
        AgriculturalEmployment = request.POST.get('AgriculturalEmployment')
        RuralPopulation= request.POST.get('RuralPopulation')
        UseSafelyDrinkingWater = request.POST.get('UseSafelyDrinkingWater')
        UseSafelySanitationServices = request.POST.get('UseSafelySanitationServices')
        UrbanPopLivinginSlums = request.POST.get('UrbanPopLivinginSlums')
        InternetUse = request.POST.get('InternetUse')

        # Load the model and make a prediction
     my_data=pd.read_csv("C:/Users/HP/Desktop/9raya/datas/zeom.csv")
     X_train = my_data[['AgriculturalEmployment', 'RuralPopulation', 'UseSafelyDrinkingWater', 'UseSafelySanitationServices', 'UrbanPopLivinginSlums', 'InternetUse']]
     X_train.columns = ['AgriculturalEmployment', 'RuralPopulation', 'UseSafelyDrinkingWater', 'UseSafelySanitationServices', 'UrbanPopLivinginSlums', 'InternetUse']
     Y_train = my_data.iloc[:198, -1]

     model = tree.DecisionTreeClassifier()
     model.fit(X_train, Y_train)

# Create a new DataFrame with the input values and column names
     X = pd.DataFrame([[AgriculturalEmployment, RuralPopulation, UseSafelyDrinkingWater, UseSafelySanitationServices, UrbanPopLivinginSlums, InternetUse]], columns=X_train.columns)

     prediction = model.predict(X)[0]
     print(prediction)

        # Render the result template with the prediction
     return render(request, 'chart.html', {'prediction': prediction})
     
     
    # Render the form template for GET requests 
     return render(request, 'chart.html')


    
      
 

    
        
        
       
    
   
   




def widget(request):
    if request.method == 'POST':
        country = request.POST['country']
        # load the training data and select relevant columns
        data = pd.read_csv('D:/Project BI/stage_are_fray_emission.csv',sep=";",header=0)

        X_train = data[['Agricultural methane emissions (% of total)', 'Agricultural nitrous oxide emissions (% of total)', 
                  'Methane emissions (% change from 1990)', 'Methane emissions (kt of CO2 equivalent)', 
                  'Methane emissions in energy sector (thousand metric tons of CO2 equivalent)', 
                  'Nitrous oxide emissions (% change from 1990)', 'Nitrous oxide emissions (thousand metric tons of CO2 equivalent)', 
                  'Nitrous oxide emissions in energy sector (% of total)', 'Other greenhouse gas emissions (% change from 1990)', 
                  'Other greenhouse gas emissions HFC PFC and SF6 (thousand metric tons of CO2 equivalent)', 
                  'Methane emissions in energy sector (thousand metric tons of CO2 equivalent)']]
        y_train = data['Total greenhouse gas emissions (kt of CO2 equivalent)']

        # train a linear regression model on the training data
        lr = LinearRegression()
        lr.fit(X_train, y_train)

        # load the data for the given country
        test_data = pd.read_csv('D:/Project BI/stage_are_fréay_emission.csv',sep=";",header=0)
        country_data = test_data[test_data['Country'] == country]

        if country_data.empty:
            return render(request, 'widget.html', {'error_message': 'Country not found'})
        
        X_test = country_data[['Agricultural methane emissions (% of total)', 'Agricultural nitrous oxide emissions (% of total)', 
                  'Methane emissions (% change from 1990)', 'Methane emissions (kt of CO2 equivalent)', 
                  'Methane emissions in energy sector (thousand metric tons of CO2 equivalent)', 
                  'Nitrous oxide emissions (% change from 1990)', 'Nitrous oxide emissions (thousand metric tons of CO2 equivalent)', 
                  'Nitrous oxide emissions in energy sector (% of total)', 'Other greenhouse gas emissions (% change from 1990)', 
                  'Other greenhouse gas emissions HFC PFC and SF6 (thousand metric tons of CO2 equivalent)', 
                  'Methane emissions in energy sector (thousand metric tons of CO2 equivalent)']]
        
        # make prediction on the given country's data
        y_pred = lr.predict(X_test)
        result = y_pred[0]/10000000
        
        return render(request, 'widget.html', {'result': result})
    return render(request, 'widget.html')
   





def form(request):
    return render(request, 'form.html')










def login(request):
    if request.method == 'POST':
        email_address = request.POST.get('email')
        password = request.POST.get('password')
        
        # Connect to the IMAP server
        try:
            mail = imaplib.IMAP4_SSL('imap.gmail.com')
            mail.login(email_address, password)
            authenticated_successfully = True
        except imaplib.IMAP4.error:
            authenticated_successfully = False

        # Check if authentication was successful
        if authenticated_successfully:
            request.session['email'] = email_address 
            request.session['password'] = password 
            return redirect('index')
        else:
            error_message = 'Incorrect email or password. Please try again.'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
  








