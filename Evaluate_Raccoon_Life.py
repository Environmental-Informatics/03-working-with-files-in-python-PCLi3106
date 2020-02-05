"""
Header Comments
File created on 02/05/2020 by Pin-Ching Li for ABE65100

Input: 2008Male0006.txt
This script is written for reading a comma separated text file: 2008Male0006.txt,
which contains the record of behavior of a raccoon whose name is George

The name, average location, distance traveled, average energy level, and the end ate of the raccoon, George, is recorded.

Output: Georges_life.txt
The behavior and characteristics of George is recorded in a test file with new format: 
str Line out put as a header block of basci information and the new tab-separated part 
for the raw data we read.

"""

import math # import math for the calculation of the quantity of raccoon behavior

def average(lst):
    Average = 0.0
    for i in lst:    
        Average = Average + i
    Average = Average/len(lst)
    return Average

def sumv(lst):
    Sum = 0
    for i in lst:
        Sum = Sum + i
    return Sum

def distance(X,Y,numbers):
    #for two list, also define the size of Distance list first 
    Dis = [0]*numbers  #define the size of Dstance with zero value
    # first distance = 0
    for i in range(len(X)-1): # loop for calculating the distance
        dX = X[i+1]- X[i] #dx
        dY = Y[i+1]- Y[i] #dy
        # distance = sqrt(dx^2+dy^2)
        distance = math.sqrt(math.pow(dX,2.0)+math.pow(dY,2.0)) 
        Dis[i+1] = distance #fill the distance list
    return Dis # return the distance list

fin   = open("2008Male00006.txt", "r") #open the file in the read mode
lines = fin.readlines() # Read the file by lines (str)
fin.close() # close the file
Data  = [0]*len(lines) # create a list of 0s of equal size to the file that was read
lastrow = len(lines)-1 # Number used to call the last row in the datasets
# Create empty list for us to store the location and energy level
X  = []
Y  = []
EnL= []
for lidx in range(len(lines)):
    if lidx == 0: 
        #First row has all the string information for the index of columns (comma separate)
        Data[lidx] = lines[lidx].strip().split(",")
    elif lidx == lastrow: #Same as firstrow
        Data[lidx] = lines[lidx].strip().split(",")
    else: # for the major part of the datasets (exclude the first and last row)
        Data[lidx] = lines[lidx].strip().split(",")
        Data[lidx][4:6]  = map(float,Data[lidx][4:6])
        Data[lidx][8:14] = map(float,Data[lidx][8:14])
        X.append(Data[lidx][4])
        Y.append(Data[lidx][5])
        EnL.append(Data[lidx][8])
   
# Calculation of average location
average_locX = average(X)
average_locY = average(Y)
#Calculation of the distance from location X, Y 
Distance     = distance(X,Y,len(lines)-2)
#Sum up the distance in the distance list
sum_distance = sumv(Distance)
#Do the average of the energy level of George
avg_energy   = average(EnL)
# Create a new dictionary with the parameters of the raccoon's characteristics and behavior
Dict_George  = {"Raccoon name":"George","Average Location":[average_locX,average_locY],
                "Distance traveled": sum_distance, "Average energy level": avg_energy,
                "Raccoon end state": Data[len(lines)-1]}
# Write the output file
with open("Georges_life.txt",'w') as file:
# Write the header first
    for key, val in Dict_George.items():
        strline = key + ":  " + str(val) + "\n"
        file.write(strline)
    file.write("\n")
    # Deal with Nested list
    for nest_list in Data:
        for val in nest_list:
            # Each Single Value output with a tab sep 
            file.write(str(val)+'\t')
        file.write('\n') # New Line indicator
    file.close() #Close file after we finished out writing