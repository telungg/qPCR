#This is what the following code does:
#1. Open .xlsx raw data file exported from qPCR machine and save it as rawData.
#2. Get unique well names from the raw data and set up necessary variables.
#3. Create a dictionary fluoDict, which correlates each well to its corresponding fluorescence values.
#4. Convert fluoDict to a new data frame sortedData.
#5. Export sortedData as .xlsx.
#6. The output file is ready to use on TSA CRAFT perl command.

#import module
import pandas as pd

#read raw data from qPCR machine .xlsx and convert it to rawData data frame.
while True:
    try:
        data = input('Enter raw data file name (without .xlsx): ') #input
        print('Opening your raw data file...')
        rawData = pd.read_excel(data+'.xlsx', sheet_name = 'Melt Curve Raw', header = 23, usecols = ['Well Position', 'Temperature', 'Fluorescence'])
        break
    except FileNotFoundError:
        print('The file does not exist. Please make sure your raw data file is on the same directory as this code.')

print('Sorting your data...')

#add variables for all wells in the plate from A1 to H12
wellName = rawData['Well Position'].unique()#.tolist()
totalWell = len(wellName)

#get the location of the highest temperature from rawData
maxTempLoc = rawData['Temperature'].argmax()

#convert data from each well from rawData into a dictionary myDict.
#Key = (string) from wellName.
#Value = (list) from Fluorescence values.
fluoDict = {}
num = 0
for well in wellName:
    fluoDict[well] = []
    fluoDict[well].extend(rawData['Fluorescence'].loc[num * maxTempLoc + num : (num+1) * maxTempLoc +num].tolist()) #list of datas associated with each temperature
    #print(num * rawData['Temperature'].argmax(), ':', (num+1) * rawData['Temperature'].argmax())
    num += 1

#create a new data frame sortedData using values from myDict
sortedData = pd.DataFrame.from_dict(fluoDict)

#add Temperature as the first column of sortedData
sortedData.insert(0, 'Temperature', '')

#add Temperature values to the Temperature column of sortedData
sortedData['Temperature'] = rawData['Temperature'].loc[:maxTempLoc]

#export sortedData to .xlsx as inputSorted.xlsx
sortedData.to_excel(data+'Sorted.xlsx', index=False)

print('Your data is now sorted and ready to use on TSA CRAFT.\nOutput = '+data+'Sorted.xlsx')
