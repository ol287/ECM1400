# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification.
# 
# This module will access data from the LondonAir Application Programming Interface (API)
# The API provides access to data to monitoring stations. 
# 
# You can access the API documentation here http://api.erg.ic.ac.uk/AirQuality/help
#
import re
import requests
import pandas
import numpy
import csv
import json
from utils import *
from matplotlib import pyplot

def get_live_data_from_api(site_code='MY1',species_code='NO',start_date=None,end_date=None):
    """
    Return data from the LondonAir API using its AirQuality API. 
    
    *** This function is provided as an example of how to retrieve data from the API. ***
    It requires the `requests` library which needs to be installed. 
    In order to use this function you first have to install the `requests` library.
    This code is provided as-is. 
    """
    import requests
    import datetime
    start_date = datetime.date.today() if start_date is None else start_date
    end_date = start_date + datetime.timedelta(days=1) if end_date is None else end_date
    
    
    endpoint = "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json"
   
    url = endpoint.format(
        site_code = site_code,
        species_code = species_code,
        start_date = start_date,
        end_date = end_date
    )
    
    res = requests.get(url)
    return res.json()


def standard_diviation():
    """
    Function that calculates the standard diviation for a given number of days
    @returns - a float which is the standard diviation
    """
    #stores all the pollution values recoreded in a list
    data=extract_values()
    mean=meannvalue(data)
    data_squared=[]
    for i in data:
        #sqaures every number in data and stores it in a new list
        data_squared.append(data[i]**2)
    sum=sumvalues(data_squared)
    number_of_items=len(data)
    standard_diviation=((sum/number_of_items)-mean)**0.5
    return standard_diviation


def linegraph():
    """
    Function that draws a line graph
    @returns - An acknowledgement message is displayed to indicate the line graph has been drawn
    """
    #stores all the pollution values recoreded in a list
    data=extract_values()
    hours=[]
    #creates a list to store the hour number corresponding to the data recorded
    for i in range(0,len(data)):
            #number of hours that has been recored is saved to a list
            hours.append(i)
    pyplot.xlabel("Hour")
    pyplot.ylabel("Pollution")
    pyplot.plot(hours,data)
    pyplot.show()
    return "Graph drawn"

def save_api_data():
    """
    Function that saves API data as a CSV file
    @returns - A 2D array is returned which contains the data that has been saved to a csv file
    """
    api_values=extract_values()
    api_times=extract_times()
    #combines the pollution recorded with its corresponding date/time
    api_data=zip(api_times,api_values)
    #new csv file is created and stored in data folder
    with open('data/api_data.csv', 'w') as file:
        writer = csv.writer(file)
        for i in api_data:
            writer.writerow(i)
    return api_data

def order_hours():
    """
    Function that saves API data in a 2D array and the array is ordered
    @returns - ordered 2D array is returned
    """
    api_values=extract_values()
    api_times=extract_times()
    api_data=[]
    #pollution values and their corresponding date/times are stored in a 2D array
    for i in range(0,len(api_times)):
        data_for_hour=[]
        data_for_hour.append(api_times[i])
        data_for_hour.append(api_values[i])
        api_data.append(data_for_hour)
    print(api_data)
    length=len(api_data)
    #bubble sort if performed on pollution values recoreded
    for i in range(0,length):
        for j in range(0,length-i-1):
            if (api_data[j][1] > api_data[j + 1][1]):
                temp=api_data[j]
                api_data[j]= api_data[j + 1]
                api_data[j + 1]= temp
    return api_data
    

def extract_values():
    """
    Functiom to get the pollution values from the JSON
    @returns - list of all the values from the JSON
    """
    api_data=get_live_data_from_api()
    raw_data=api_data["RawAQData"]
    data=raw_data["Data"]
    listofvalues=[]
    for i in data:
        if i["@Value"]=='':
            #if the value is unrecorded zero is appended to the list
            listofvalues.append(0)
        else:
            float_value=float(i["@Value"])
            listofvalues.append(float_value)
    return listofvalues

def extract_times():
    """
    Functiom to get the date/time values from the JSON
    @returns - list of all the dates/times from the JSON
    """    
    a=get_live_data_from_api()
    b=a["RawAQData"]
    c=b["Data"]
    listoftimes=[]
    for i in c:
        print(i["@MeasurementDateGMT"])
        listoftimes.append(i["@MeasurementDateGMT"])
    return listoftimes


