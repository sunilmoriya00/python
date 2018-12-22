import os

file_path = input("Enter input file path: ")
search_item = r'X-DSPAM-Confidence'

mylist = [] #Empty list to accumulate all the float data
total_lines = 0  # variable initialization with default value
addition = 0    # variable initialization with default value

with open(file_path,'r') as f1:     #Open file in read only mode
    data = f1.read()                #Read whole file
    for item in data.split("\n"):   #Iterate read data and remove new line charecter
        if search_item in item:
            total_lines = total_lines + 1  #Get total count of lines where search_item is present
            data1 = item.strip("\\")    #remove \\ from output
            data2 = data1.split(":")    #Separate data based on ':'
            final_data = float(data2[-1]) # convert data to float
            mylist.append(final_data)       #Add output data to list

for element in mylist:  # Iterate list to get sum
    addition += element

avg = float(addition/total_lines)
print("Total lines with {} in input file are: {}".format(search_item, total_lines))
print("Average of all float values is: {}".format(avg))
