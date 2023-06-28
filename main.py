# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification
from monitoring import *
from reporting import *
from intelligence import *
from time import *

def main_menu():
    """
    Function that will start program, showing the main menu of the program allowing the user to navigate through the different options.
    """
    # Your code goes here
    # Five meny options will be presented to the user
    print("R - Access the PR module \nI - Access the MI module \nM - Access the RM module \nA - Print the About text \nQ - Quit the application \n")
    option=input("Choose a menu option")
    # If the user does not enter a valid menu option they will be asked to try again until they do
    while option!=("R"or"I"or"M"or"A"or"Q"):
        option=input("Choose a VALID main menu option")
    if option=="R":
        reporting_menu()
    elif option=="I":
        intelligence_menu()
    elif option=="M":
        monitoring_menu()
    elif option=="A":
        about()
    elif option=="Q":
        quit()
    else:
        print("invalid option")
        main_menu()

def reporting_menu():
    """
    A function that will be executed when the user chooses the ‘R‘ option in the main menu,
    allowing the user to access the functions in the reporting module, then user will be taken back to the main menu
    """
    # Your code goes here
    # Seven meny options will be presented to the user
    print("DA-Daily Average\nDM-Daily Median\nHA-Hourly Average\nMA-Monthly Average\nPH-Peak Hour Data\nCM-Count Missing Data\nFM-Fill Missing Data" )
    option=input("Choose a reporting menu option")
    # If the user does not enter a valid menu option they will be asked to try again until they do
    while option!=("DA"or"DM"or"HA"or"MA"or"PH"or"CM"or"FM"):
        option=input("Choose a VALID reporting menu option")
    data=None
    # Function is called to get the users preferences for which monitoring station and pollutant they are interested in  
    monitoring_station,pollutant=Get_Information_for_Reporting()
    if option=="DA":
        data=daily_average(data,monitoring_station,pollutant)
    elif option=="DM":
        data=daily_median(data,monitoring_station,pollutant)
    elif option=="HA":
        data=hourly_average(data,monitoring_station,pollutant)
    elif option=="MA":
        data=monthly_average(data,monitoring_station,pollutant)
    elif option=="PH":
        date=input("enter a date in the form : year-month-day e.g. 2021-01-01")
        data=peak_hour_date(data,date,monitoring_station,pollutant)
    elif option=="CM":
        data=count_missing_data(data,monitoring_station,pollutant)
    elif option=="FM":
        newvalue=input("enter a new value")
        data=fill_missing_data(data,newvalue,monitoring_station,pollutant)
    # Data is displayed
    # User is then taken back to the main menu page
    print(data)
    main_menu()



def monitoring_menu():
    """
    A function that will be executed when the user chooses the ‘M‘ option in the main menu,
    allowing the user to access the functions in the Monitoring module, then user will be taken back to the main menu
    """
    # Your code goes here
    # Four meny options will be presented to the user
    print("O - Order hours in asending order by pollution level\nL - Line graph\nS-Standard Diviation\nF-Save API data to a text file")
    option=input("Choose a menu option")
    # If the user does not enter a valid menu option they will be asked to try again until they do
    while option!=("O"or"L"or"S"or"F"):
        option=input("Choose a VALID reporting menu option")
    if option=="O":
        data=order_hours()
    elif option=="L":
        data=linegraph()
    elif option=="S":
        data=standard_diviation()
    elif option=="F":
        data=save_api_data()
    # Data is displayed
    # User is then taken back to the main menu page
    print(data)
    main_menu()



def intelligence_menu():
    """
    A function that will be executed when the user chooses the ‘I‘ option in the main menu,
    allowing the user to access the functions in the Intelligence module, then user will be taken back to the main menu
    """
    # Your code goes here
    # Four meny options will be presented to the user
    print("R - Find red pixels\nC - Find cyan pixels \nCC - Detect connected componets \nCCS - Detect connected componets sorted \n")
    option=input("Choose a menu option")
    # If the user does not enter a valid menu option they will be asked to try again until they do
    while option!=("R"or"C"or"CC"or"CCS"):
        option=input("Choose a VALID inteligent menu option")
    if option=="R":
        data=find_red_pixels()
    elif option=="C":
        data=find_cyan_pixels()
    elif option=="CC":
        print("Connected components for C(Cyan pixels) or R(Red pixels)")
        colour_option=input("Enter C or R")
        # If the user does not enter a valid menu option they will be asked to try again until they do
        while option!=("R"or"C"):
            print("invalid input")
            colour_option=input("Enter C or R")
        if colour_option=="C":
            # JPEG containing the cyan pixels is created
            find_cyan_pixels()
            # Assigns image as the file path for cyan pixel JPEG
            IMG="data/map-cyan-pixels"
        else:
            # JPEG containing the red pixels is created
            find_red_pixels()
            # Assigns image as the file path for red pixel JPEG
            IMG="data/map-red-pixels"
        data=detect_connected_components(IMG)
    elif option=="CCS":
        data =detect_connected_components_sorted()
        print("detect connected components sorted for C(Cyan pixels) or R(Red pixels)")
        colour_option=input("Enter C or R")
        # If the user does not enter a valid menu option they will be asked to try again until they do
        while option!=("R"or"C"):
            print("invalid input")
            colour_option=input("Enter C or R")
        if colour_option=="C":
            # JPEG containing the cyan pixels is created
            find_cyan_pixels()
            # Assigns image as the file path for cyan pixel JPEG
            IMG="data/map-cyan-pixels"
        else:
            # JPEG containing the red pixels is created
            find_red_pixels()
            # Assigns image as the file path for red pixel JPEG
            IMG="data/map-red-pixels"
        MARK=detect_connected_components(IMG)
        data=detect_connected_components_sorted(MARK)    
    # Data is displayed
    # User is then taken back to the main menu page
    print(data)
    main_menu()
    



def about():
    """
    A function that will be executed when the user chooses the A option in the main menu. 
    Prints the module code (ECM1400 ) and a string with my 6-digits candidate number,
    then the user is taken back to the main menu.
    """
    # Your code goes here
    print("Module code: ECM1400")
    print("Candidate Number: 250633")
    # User is then taken back to the main menu page
    main_menu()

def quit():
    """
    Function to terminate the program
    """
    # Your code goes here
    print("program will be terminated")
    exit()

def Get_Information_for_Reporting():
    """"
    Function that gets the montoring station and pollutant the user wants information about 
    """
    # Your code goes here
    # User is asked to choose one the the three monotoring stations
    monitoring_station=input("Enter a montoring station:Harlington,Marylebone,Kensington")
    # If the user does not enter a valid menu option they will be asked to try again until they do
    while monitoring_station!=("Harlington"or"Marylebone"or "Kensington"):
        print("Enter a valid monitoring station name")
        monitoring_station=input("Choose a montoring station")
    # User is asked to choose one the the three pollutants
    pollutant=input("Enter a pollutant : no,pm10,pm25")
    # If the user does not enter a valid menu option they will be asked to try again until they do
    while pollutant!=("no"or"pm10"or"pm25"):
        print("Enter a valid pollutant name")
        pollutant=input("Enter a pollutant : no,pm10,pm25")
    return monitoring_station,pollutant

if __name__ == '__main__':
    main_menu()