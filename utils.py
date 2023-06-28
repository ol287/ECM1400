# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification


def sumvalues(values):   
    """
    Function to calculate the sum of all the values in a list/array
    @param values - a list 
    @returns - the sum of all the values in the list
    """    
    try:
        sum=0
        #iterates through the list of values taken as a parameter
        for i in values:
            sum=sum+float(i)
        return sum
    except:
        print("exception has occured due to non-numerical value in list")


def maxvalue(values):
    """
    Function to find the index of the maximum value in a list/array
    @param values - a list 
    @returns - the index of the maximum value in the list
    """  
    try:
        #max value is set to the first item in the list
        max_value=values[0]
        #iterates through the list of values taken as a parameter
        for i in values:
            #checks if item is a number
            a=float(i)
            #if an item in the list is greater than the value assigned to max
            if i>max_value:
                max_value=i 
        #index of the maximum value in the list is returned
        return values.index(max_value)
    except:
        print("exception has occured due to non-numerical value in list")


def minvalue(values):
    """
    Function to find the index of the minimum value in a list/array
    @param values - a list 
    @returns - the index of the minimum value in the list
    """  
    try:
        #min value is set to the first item in the list
        min_value=values[0]
        #iterates through the list of values taken as a parameter
        for i in values:
            #checks if item is a number
            a=float(i)
            #if an item in the list is less than the value assigned to max
            if i<min_value:
                min_value=i 
        #index of the minimum value in the list is returned
        return values.index(min_value)
    except:
        print("exception has occured due to non-numerical value in list")

def meannvalue(values):
    """
    Function to calculate the mean value of a list/array
    @param values - a list 
    @returns - the mean value of all the items in the list
    """ 

    try:
        sum=0
        n=len(values)
        for i in values:
            sum=sum+i
        #sum of list is divided by the number of values in the list
        mean=sum/n
        return mean
    except:
        print("exception has occured due to non-numerical value in list")

def countvalue(values,x):
    """
    Function to count how many times a value x appears in a list/array 
    @param values - a list 
    @param x - an element
    @returns - the number of times the element x appears in values 
    """    
    ## Your code goes here
    count=0
    for i in values:
        #compares each element in values with the value x
        if x==i:
            count=count+1
    return count


