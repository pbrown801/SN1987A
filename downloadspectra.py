# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 13:48:35 2020

@author: Christopher
"""

# This program is able to get data from the Open Supernova catalog, specifically the wavelength and flux of each spetra of a desired supernova
# Creates an new file for each spetra of the supernova that contains its wavelength and flux in the same folder this program is, so beware where you run this program in because it will create a lot of files
from urllib import request

# Allows User to input the desired supernova
SNname = input("Enter SuperNova Name: ")
firstUrl = "https://api.astrocats.space/" + str(SNname) + "/spectra/time?format=csv"

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

file2 = open("SNData1.csv","r")

values = []
for row in file2:
    values += [row.split(",")]

values.pop(0)

spectra = []
for i in values:
    spectra.append(float(i[1]))
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
    file.close()

file2.close()

print("DONE")








