import pytest
import pandas
from intelligence import *
from utils import *
from reporting import *
from monitoring import *
from main import *

"""test data"""

"""Utility functions testing"""

#test case 1 for sumvalues function
def test_sumvalues_1():
    #boundary data
    assert utils.sumvalues(values=[]) == 0

#test case 2 for sumvalues function
def test_sumvalues_2():
    #normal data
    assert utils.sumvalues(values=[1,2,3]) == 6

#test case 3 for sumvalues function
def test_sumvalues_3():
    #erroneous data
    assert utils.sumvalues(values=["a","b","c"]) == print("exception has occured due to non-numerical value in list")

#test case 1 for maxvalue function
def test_maxvalue_1():
    #boundary data
    assert utils.maxvalue(values=[]) == print("exception has occured due to non-numerical value in list"), None

#test case 2 for maxvalue function
def test_maxvalue_2():
    #normal data
    assert utils.maxvalue(values=[1,2,3]) == 2


#test case 3 for maxvalue function
def test_maxvalue_3():
    #erroneous data
    assert utils.maxvalue(values=["a","b","c"]) == print("exception has occured due to non-numerical value in list"), None


#test case 1 for minvalue function
def test_minvalue_1():
    #boundary data
    assert utils.minvalue(values=[]) == print("exception has occured due to non-numerical value in list"), None

#test case 2 for minvalue function
def test_minvalue_2():
    #normal data
    assert utils.minvalue(values=[1,2,3]) == 0


#test case 3 for minvalue function
def test_minvalue_3():
    #erroneous data
    assert utils.minvalue(values=["a","b","c"]) == print("exception has occured due to non-numerical value in list"), None

#test case 1 for meanvalue function
def test_meanvalue_1():
    #boundary data
    assert utils.meannvalue(values=[]) == print("exception has occured due to non-numerical value in list"), None

#test case 2 for meanvalue function
def test_meanvalue_2():
    #normal data
    assert utils.meannvalue(values=[1,2,3]) == 2


#test case 3 for meanvalue function
def test_meanvalue_3():
    #erroneous data
    assert utils.meannvalue(values=["a","b","c"]) == print("exception has occured due to non-numerical value in list"), None

#test case 1 for countvalue function
def test_countvalue_1():
    #boundary data
    assert utils.countvalue(values=[],x=" ") == 0

#test case 2 for countvalue function
def test_countvalue_2():
    #normal data
    assert utils.countvalue(values=[1,2,3],x=1) == 1


#test case 3 for countvalue function
def test_countvalue_3():
    #erroneous data
    assert utils.countvalue(values=["a","b","c"],x="a") == 1


#test case 1 for daily average function
def test_dailyaverage_1():
    #normal data
    assert len(daily_average(data=None,monitoring_station="Harlington", pollutant="no"))==365

#test case 1 for daily median function
def test_dailymedian_1():
    #normal data
    assert len(daily_median(data=None,monitoring_station="Harlington", pollutant="no"))==365

#test case 1 for hourly average function
def test_hourlyaverage_1():
    #normal data
    assert len(hourly_average(data=None,monitoring_station="Harlington", pollutant="no"))==24

#test case 1 for monthly average function
def test_monthlyaverage_1():
    #normal data
    assert len(monthly_average(data=None,monitoring_station="Harlington", pollutant="no"))==12

#test case 1 for peak hour data function
def test_peak_hour_data_1():
    #normal data
    assert peak_hour_date(data=None,date="2021-01-01",monitoring_station="Harlington", pollutant="no")=="19:00, 13.00595"

#test case 1 for peak hour data function
def test_count_missing_data_1():
    #normal data
    assert count_missing_data(data=None,  monitoring_station="Harlington",pollutant="no") == 70

#test case 1 for peak hour data function
def fill_missing_data_1():
    #normal data
    assert len(fill_missing_data(data=None,new_value=10,  monitoring_station="Harlington",pollutant="no")) == 8760
    assert type(fill_missing_data(data=None,new_value=10,  monitoring_station="Harlington",pollutant="no")) == pandas.core.frame.DataFrame

#test case 1 for find red pixel function
def find_red_pixel_1():
    #normal data
    assert len(find_red_pixels(map_filename="map.png", upper_threshold=100, lower_threshold=50))==1140
    assert type(find_red_pixels(map_filename="map.png", upper_threshold=100, lower_threshold=50))==numpy.ndarray

#test case 1 for find cyan pixel function
def find_cyan_pixel_1():
    #normal data
    assert len(find_cyan_pixels(map_filename="map.png", upper_threshold=100, lower_threshold=50))==1140
    assert type(find_cyan_pixels(map_filename="map.png", upper_threshold=100, lower_threshold=50))==numpy.ndarray

#test case 1 for find connected components function
def test_connected_components_1():
    #normal data
    assert len(detect_connected_components(IMG="data/map-cyan-pixels"))==1140
    assert len(detect_connected_components(IMG="data/map-red-pixels"))==1140

#test case 1 for find standard diviation function
def test_standard_diviation_1():
    #normal data
    assert type(standard_diviation())==list

#test case 1 for line graph function
def test_linegraph_1():
    #normal data
    assert linegraph()=="Graph drawn"



