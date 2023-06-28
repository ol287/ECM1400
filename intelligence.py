# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification

import skimage.io
import numpy 
import pandas
import matplotlib.pyplot as plt
import utils

  
def find_red_pixels(map_filename="map.png", upper_threshold=100, lower_threshold=50):
    """
    Function that returns a 2D array in numpy representing the output binary image of red pixels and writes the 2D array into a file named as map-red-pixels.jpg.
    @param map_filename - assigned the filename of the file that is to be opened, string
    @param upper_threshold - assigned to compare the RGB values to, integer
    @param lower_threshold - assigned to compare the RGB values to, integer
    @return numpy 2D array containing only the red pixels as white pixel values
    """
    #png image file of map is opened
    image=skimage.io.imread(fname="data/"+map_filename)
    imagearr=convert_png_to_2d_array(image)
    blackpixel=numpy.array([0,0,0])
    whitepixel=numpy.array([1,1,1])
    redpixelarr=[]
    #each pixel in the image is chekcked to see if it is red, if so a white pixel is saved to the new array
    for row in imagearr:
        rowarr=[]
        for collum in row:
            #checks if pixel is red
            if (collum[0]>upper_threshold) and (collum[1]<lower_threshold) and (collum[2]<lower_threshold):
                rowarr.append(whitepixel)
            else:
                rowarr.append(blackpixel)
        redpixelarr.append(rowarr)
    redpixelarr = numpy.array(redpixelarr)
    skimage.io.imsave("data/map-red-pixels.jpeg",redpixelarr)
    return redpixelarr


def find_cyan_pixels(map_filename="map.png", upper_threshold=100, lower_threshold=50):
    """"
    Function that returns a 2D array in numpy representing the output binary image of cyan pixels and writes the 2D array into a file named as map-cyan-pixels.jpg.
    @param map_filename - assigned the filename of the file that is to be opened, string
    @param upper_threshold - assigned to compare the RGB values to, integer
    @param lower_threshold - assigned to compare the RGB values to, integer
    @return numpy 2D array containing only the cyan pixels as white pixel values
    """
    #png image file of map is opened
    image=skimage.io.imread(fname="data/"+map_filename)
    imagearr=convert_png_to_2d_array(image)
    blackpixel=numpy.array([0,0,0])
    whitepixel=numpy.array([1,1,1])
    cyanpixelarr=[]
    for row in imagearr:
        rowarr=[]
        for collum in row:
            #checks if pixel is cyan
            if (collum[0]<lower_threshold) and (collum[1]>upper_threshold) and (collum[2]>upper_threshold):
                rowarr.append(whitepixel)
            else:
                rowarr.append(blackpixel[0:3])
        cyanpixelarr.append(rowarr)
    cyanpixelarr = numpy.array(cyanpixelarr)
    skimage.io.imsave("data/map-cyan-pixels.jpeg",cyanpixelarr)
    return cyanpixelarr




def detect_connected_components(IMG):
    """"
    Function that reads IMG returned from Task MI-1, returns a 2D array in numpy MARK and writes the number of pixels inside each connected component region into a text file cc-output-2a.txt.
    @param IMG - assigned the filename of the jpeg file that is to be opened, string
    @return numpy 2D array
    """
    #loads the image and converts it into a 3D numpy array
    IMG=plt.imread(IMG+'.jpeg')
    shape=IMG.shape
    MARK=numpy.zeros((shape[0],shape[1]),numpy.uint16)
    Q=numpy.ndarray((0,2))
    # component_number stores the number of which component is being checked
    component_number=1
    componet_lengths=[]
    for x in range(len(IMG)):
        for y in range(len(IMG[0])):
            pixel=IMG[x][y]
            #checks if the pixel is not black and hasn't been visited
            if utils.sumvalues(list(pixel))>255 and MARK[x][y]<=0:
                #Marks the comoponent has been visted
                MARK[x][y]=component_number
                #component size is sent to one
                component_size=1
                #Q is a numpy array that stores the cooridinated of pixels in a given connected component
                Q=numpy.append(Q,[[x,y]],axis=0)
                #Every pixel in Q is checked
                while len(Q)>0:
                    #mn is set as the last pixel in Q
                    m_n=[int(Q[-1][0]),int(Q[-1][1])]
                    #pop pixel from Q
                    Q=numpy.delete(Q,-1,axis=0)
                    #checks all the pixels to see if they are not black around a given pixel
                    for s in range(m_n[0]-1,m_n[0]+2):
                        for t in range(m_n[1]-1,m_n[1]+2):
                            if 0<s<shape[0] and 0<t<shape[1]:
                                j=IMG[s][t]
                                #checks if the pixel is not black and hasn't been visited
                                if utils.sumvalues(list(j))>255 and MARK[s][t]<=0:
                                    #pixel is set as visted
                                    MARK[s][t]=component_number
                                    #new discovered connected pixel is added to Q
                                    Q=numpy.append(Q,[[s,t]],axis=0)
                                    #size of component is increased by one
                                    component_size=component_size+1
                componet_lengths.append([component_number,component_size])
                component_number=component_number+1
    write_component_to_file(componet_lengths,"./data/cc-output-2a.txt")
    return MARK

def detect_connected_components_sorted(MARK):
    """
    Function that reads MARK retured from detect_contected_componets() 
    and writes all connected components in descending order into a text file cc-output-2b.txt,
    largest two compinets are written into a JPEG file 
    @param MARK - 2D numpy array
    @return numpy 2D array contain the data
    """
    # Your code goes here
    length_of_components=find_component_lengths(MARK)
    #components are ordered in descending order 
    sorted_length_of_components=sort_2d_array(length_of_components)
    blackpixel=numpy.array([0,0,0])
    whitepixel=numpy.array([255,255,255])
    shape=MARK.shape
    top_2=numpy.empty((shape[0],shape[1],3),numpy.uint8)
    #Iterates through mark to find the largest two componets
    for x in range(len(MARK)):
        for y in range(len(MARK[0])):
            #checks if the componet is the first or second position in sorted_length_of_components
            if MARK[x][y]==sorted_length_of_components[0][0] or MARK[x][y]==sorted_length_of_components[1][0]:
                top_2[x][y]=whitepixel
            else:
                top_2[x][y]=blackpixel
    #list of components in descending order is saved
    write_component_to_file(sorted_length_of_components,"./data/cc-output-2b.txt")
    #largest two components are saved into a JPEG
    plt.imsave("./data/cc-top-2.jpeg",top_2)
    data="file 'cc-top-2' and 'cc-output-2b' saved"
    return data





def find_component_lengths(MARK):
    """
    Function to find the length of components by size
    @param MARK - list of components by size, 2D array
    @return - list of component lengths
    """
    #expecting list of components by size
    #MARK which is a 2D array is 'flattened' to be a 1D array
    mark_1d=MARK.flatten()
    sorted_set=find_unique_values(mark_1d)
    component_length=[]
    for i in range(1,len(sorted_set)):
        component_length.append([i,0])

    for x in range(MARK.shape[0]):
        for y in range(MARK.shape[1]):
            p=MARK[x][y]
            if p!=0:
                for i in sorted_set:
                    if i==p:
                        component_length[i-1][1]+=1
    return component_length

def convert_png_to_2d_array(image):
    """"
    Funciton that saves a png image's pixels to a 2D array
    @param image - stores a thec pixels from a png file in a numpy array
    @returns - 2D array
    """

    # Your code goes here
    imagearr=[]
    for i in image:
        arr=[]
        for j in i:
            arr.append(j)
        imagearr.append(arr)
    return imagearr

def write_component_to_file(values, filename):
    """"
    Funciton that writes a list of connected components to a file
    @param values - 2D array that contains lists which have 2 elements: component number and number of pixels
    @param filename - a string containing the file which is to be written to
    """
    # Your code goes here
    file = open(filename, "w")
    #writes each component and its corresponding number and number of pixels to a text file
    for i in range(len(values)):
        file.write('Connected Component '+str(values[i][0])+', number of pixels = '+str(values[i][1]))
        file.write('\n')
    file.close()

def find_unique_values(list):
    """"
    Funciton that returns a list/array of only unique values from a list
    @param list- list contains a list of elements
    """
    # Your code goes here
    unique_values=[]
    #every item in the list is checked
    for i in list: 
        # Checks if the element is already in the list
        if i not in unique_values: 
            unique_values.append(i) 
    return unique_values



def sort_2d_array(array):
    """"
    Funciton that sorts a 2d array in descending order
    @param array - a 2D array
    @returns - a 2D array is retured that orders each list in the array based on the first element in descending order
    """
    # Your code goes here
    #length is assigned to the number of rows
    length=len(array)
    for i in range(0,length):
        for j in range(0,length-i-1):
            # if an element is less than its adjacent one, they are swapped
            if (array[j][1] < array[j + 1][1]):
                temp=array[j]
                array[j]= array[j + 1]
                array[j + 1]= temp
    return array


