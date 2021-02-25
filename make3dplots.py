# -*- coding: utf-8 -*-
"""
Created on Thu May  7 17:52:01 2020

@author: Christopher
"""

# This program is able to get data from the Open Supernova catalog and create a 3-D plot of Wavelength, Flux, and MJD
from urllib import request
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Allows User to input the desired supernova
SNname = input("Enter SuperNova Name: ")
firstUrl = "https://api.astrocats.space/" + str(SNname) + "/spectra/time?format=csv"

#################################################################################################

# This function graphs the data into a 3-D plot
def graph(file):
    file = open(file, 'r')
    values = []
    for row in file:
        values += [row.split(",")]
    
    values.pop(0)
    wavelength = []
    flux = []
    for i in values:
        wavelength.append(float(i[0]))
        flux.append(float(i[1]))
    
    MJDfile = open("SNData2.csv", 'r')

    values2 = []
    for rr in MJDfile:
        values2 += [rr.split(",")]
    
    values2.pop(0)
    
    MJD = []
    for ii in values:
        MJD.append(float(i[1]))
    ax.plot3D(wavelength,wavelength,flux,color=np.random.rand(3))

#################################################################################################

# This function downloads the data from sne.space
def download(csvUrl):
    #goes to url and stores connection with url
    responce = request.urlopen(csvUrl)
    # read data from url
    csv = responce.readlines()
    csv_decoded = []
    for elem in csv:
        csv_decoded.append(elem.decode('utf-8'))
              
    # Allows user to make the name of the file that will be created as a csv file
    url_file = "SNData1.csv" 
    file = open(url_file,"w")
    
    #Puts lines into the new files created   
    for i in csv_decoded:
        file.write(i)
    file.close()

download(firstUrl)

#############################################################################################

# Here I label the axis of the 3-D plot
ax = plt.axes(projection="3d")
ax.set_xlabel('Wavelength (Å)')
ax.set_ylabel('Modified Julian Date (Years)')
ax.set_zlabel('Flux')
ax.set_title('Wavelength vs Flux vs Modified Julian Date')

##############################################################################################

file2 = open("SNData1.csv","r")

values = []
for row in file2:
    values += [row.split(",")]

values.pop(0)

spectra = []
for i in values:
    spectra.append(float(i[1]))
# I print the spectras to make sure it is the right supernova
print(spectra)

for j in spectra:
    secondUrl = "https://api.astrocats.space/SN1987A/spectra/data?time=" + str(j) + "0&closest&format=csv"
    #goes to url and stores connection with url
    responce = request.urlopen(secondUrl)
    # read data from url
    csv = responce.readlines()
    csv_decoded = []
    for elem in csv:
        csv_decoded.append(elem.decode('utf-8'))
         
    # Allows user to make the name of the file that will be created as a csv file
    url_file = str(SNname) + "_" + str(j) + ".csv" 
    file = open(url_file,"w")
    
    #Puts lines into the new files created   
    for k in csv_decoded:
        file.write(k)
    graph(url_file)
    file.close()

file2.close()

print("DONE")