# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification
import numpy as np
from utils import *
import datetime
import pandas as pd
import csv

def daily_average(data,monitoring_station, pollutant):
    """Function that returns a list/array with the daily averages for a particular pollutant and monitoring station."""
    ## Your code goes here
    averagelist=[]
    #function is called to open the csv file for a given montoring station
    #varibale data stores a pandas dataframe
    data=opencsv(monitoring_station)
    #converts the collumn of a given polluant to a list from the pandas dataframe
    values=data[pollutant].tolist()
    #every item in values is iterated through
    for i in range(0,365):
        #list to store the 24 values obsereved in a day
        values_for_a_day=[]
        for j in range(0,23):
            try:
                values_for_a_day.append(float(values[i]))
            except:
                #if item is no data then zero is added to the list of values for a given day
                values_for_a_day.append(float(0))
        #mean of values for a single day is added to the average list
        mean=meannvalue(values_for_a_day)
        averagelist.append(mean)
    return averagelist



def daily_median(data, monitoring_station, pollutant):
    """Function that returns a list/array with the daily median for a particular pollutant and monitoring station."""
    ## Your code goes here
    medianlist=[]
    #function is called to open the csv file for a given montoring station
    #varibale data stores a pandas datafram
    data=opencsv(monitoring_station)
    #converts the collumn of a given polluant to a list from the pandas dataframe
    values=data[pollutant].tolist()
    #every item in values is iterated through
    for i in range(0,365):
        #list to store the 24 values obsereved in a day
        values_for_a_day=[]
        for j in range(0,23):
            try:
                values_for_a_day.append(float(values[i]))
            except:
                #if item is no data then zero is added to the list of values for a given day
                values_for_a_day.append(float(0))
        #values in list are ordered
        values_for_a_day.sort()
        #middle value of ordered list is stored as the median
        if len(values_for_a_day)%2==1:
            median=values_for_a_day[len(values_for_a_day)//2]
        else:
            median=(values_for_a_day[(len(values_for_a_day)+2)//2]+values_for_a_day[(len(values_for_a_day))//2])/2
        medianlist.append(median)
    return medianlist




def hourly_average(data, monitoring_station, pollutant):
    """Function that returns a list/array with the hourly averages for a particular pollutant and monitoring station."""
    ## Your code goes here
    hourlyaveragelist=[]
    #function is called to open the csv file for a given montoring station
    #varibale data stores a pandas datafram
    data=opencsv(monitoring_station)
    #converts the collumn of a given polluant to a list from the pandas dataframe
    values=data[pollutant].tolist()
    #every item in values is iterated through
    hour=1
    while hour<25:
        row=hour
        values_for_a_given_hour=[]
        for day in range(0,364):
            try:
                values_for_a_given_hour.append(float(values[row]))
            except:
                #if item is no data then zero is added to the list of values for a given day
                values_for_a_given_hour.append(float(0))
            row=row+24
        hourlyaveragelist.append(meannvalue(values_for_a_given_hour))
        hour=hour+1
    return hourlyaveragelist
    

def monthly_average(data, monitoring_station, pollutant):
    """Function that returns a list/array with the monthly averages for a particular pollutant and monitoring station."""
    # Your code goes here
    # Collumn number of pollutant is assigned to index
    index=get_pollutant_index(pollutant)
    # CSV file of a given monitoring station
    data= opencsv_as_2D_array(monitoring_station)
    dict_monthly_average={}
    #iterate through the data stored
    for i in range(1,len(data)):
        #checks if the month is in the dictionary 
        if (data[i][0])[5:7] in dict_monthly_average:
            try:
                dict_monthly_average[(data[i][0])[5:7]].append(float(data[i][index]))
            except:
                #if the value is not a number ie "no data" then 0 is saved as the value instead
                dict_monthly_average[(data[i][0])[5:7]].append(float(0))
            continue
        else:
            dict_monthly_average.update({(data[i][0])[5:7]: [data[i][index]]})
    for k in dict_monthly_average:
        #l stores all the values for a given month
        l=dict_monthly_average[k]
        for i in range(0,len(l)-1):
            if l[i]=="No data":
                l[i]=0
            else:
                l[i]=float(l[i])
        #average is calculated for each month
        avg=meannvalue(l)
        dict_monthly_average[k]=avg
    return list(dict_monthly_average.values())
    






def peak_hour_date(data, date, monitoring_station,pollutant):
    """Function that returns the hour of the day with the highest pollution level and its corresponding value for a given date"""
    ## Your code goes here
    #function is called to open the csv file for a given montoring station
    #varibale data stores a pandas datafram
    data=opencsv(monitoring_station)
    values=data[pollutant].tolist()
    dates=data["date"]
    index=0
    while dates[index]!=date:
        index=index+1
    values_for_a_given_day=[]
    for i in range(0,24):
        try:
            values_for_a_given_day.append(float(values[index]))
        except:
            #if item is no data then zero is added to the list of values for a given day
            values_for_a_given_day.append(float(0))
        index=index+1
    max=maxvalueoflist(values_for_a_given_day)
    hour=0
    for i in values_for_a_given_day:
        if i ==max:
            break
        hour=hour+1
    date_and_max=str(hour)+":00, "+ str(max)
    return date_and_max
    


def count_missing_data(data,  monitoring_station,pollutant):
    """Function for a given monitoring station and pollutant, returns the number of No data entries are there in the data."""
    ## Your code goes here
    no_data_entries=0
    #function is called to open the csv file for a given montoring station
    #varibale data stores a pandas dataframe
    data=opencsv(monitoring_station)
    values=data[pollutant].tolist()
    #iterates through every item stored in values and checks if the value assigned is "No Data"
    for i in values:
        if i=="No data":
            no_data_entries=no_data_entries+1
    return no_data_entries



def fill_missing_data(data, new_value,  monitoring_station,pollutant):
    """Function for a given monitoring station and pollutant, returns a copy of the data with the missing values No data replaced by the value in the parameter new value."""
    ## Your code goes here
    #function is called to open the csv file for a given montoring station
    #varibale data stores a pandas dataframe
    data=opencsv(monitoring_station)
    values=data[pollutant].tolist()
    #iterates through every item stored in values and checks if the value assigned is "No Data"
    for i in range(0,len(values)-1):
        if values[i]=="No data":
            #if the element is "No data", then this element's value is updated to the new value in the pandas dataframe
            data.at[i,pollutant]=new_value
    return data
    



def maxvalueoflist(list):
    """Function that returns the maximum value of a list"""
    #maximum value is assigned as the first element in the list
    maxvalue=list[0]
    #every item in the list is checked 
    #if item is larger than the value assgiend to the variable maxvalue then the value of maxvalue is reassigned
    for i in range(0,len(list)):
        if list[i]>maxvalue:
            maxvalue=list[i]
    return maxvalue

def minvalueoflist(list):
    """Function that returns the minimum value of a list"""
    #minimum value is assigned as the first element in the list
    minvalue=list[0]
    #every item in the list is checked 
    #if item is less than the value assgiend to the variable maxvalue then the value of maxvalue is reassigned
    for i in range(0,len(list)):
        if list[i]<maxvalue:
            minvalue=list[i]
    return minvalue

def opencsv(monitoring_station):
    """Function that opens the csv file and returns a pandas data frame for a given monotoring station"""
    data_files={
    "Harlington":pd.read_csv("data/Pollution-London Harlington.csv"),
    "Marylebone":pd.read_csv("data/Pollution-London Marylebone Road.csv"),
    "Kensington":pd.read_csv("data/Pollution-London N Kensington.csv")
    }
    data=data_files[monitoring_station]
    return data

def opencsv_as_2D_array(monitoring_station):
    with open ("data/Pollution-London Harlington.csv", newline="") as csvfile:
        dataH=list(csv.reader(csvfile))
    with open ("data/Pollution-London Marylebone Road.csv", newline="") as csvfile:
        dataM=list(csv.reader(csvfile))
    with open ("data/Pollution-London N Kensington.csv", newline="") as csvfile:
        dataK=list(csv.reader(csvfile))
    data_files={
    "Harlington":dataH,
    "Marylebone":dataM,
    "Kensington":dataK
    }
    data=data_files[monitoring_station]
    return data

def get_pollutant_index(pollutant):
    pollutant_dict={
        "no":2,
        "pm10":3,
        "pm25":4
    }
    index=pollutant_dict[pollutant]
    return index



