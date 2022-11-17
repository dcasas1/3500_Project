# CMPS 3500 - Class Project
# GROUP 8
#
# MEMBERS:
# David Casas
# Jonathan Soto
# Michaelted Acosta
# Nicklas Chiang
######################################################

import csv
import statistics
import math
import collections
import os

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # Creating Variables
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # We check which value from the start of each list is smaller
            
            # If beginning item of left list is smaller, add to sorted list
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
                
            # Else, beginning item of right list is smaller, add to sorted list
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        #If end of left list, add elements from right list
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
            
      #If end of left list, add elements from right list
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list

# Function for merge sorting
def merge_sort(nums):
    # Return if single element list
    if len(nums) <= 1:
        return nums

    # Use floor division to get midpoint, indices must be integers
    mid = len(nums) // 2

    # Sort and merge each list
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Merge into new list
    return merge(left_list, right_list)

#checks to see if the value can be converted to float from string
def is_number(temp):
    try:
        float(temp)
        return True
    except ValueError:
        return False

fileName = input("Please enter the name of the file: ")
with open(fileName, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    headings = next(spamreader)
    #checks to see if the file is empty
    if(len(headings)):
        print()
    else:
        raise ValueError('---File is empty---')
    rows = []
    for row in spamreader:
        temp = []
        for column in range(0, len(row)):
            if(is_number(row[column])):
                temp.append(float(row[column]))
        rows.append(temp)

# Function to find all unique values of the list
def unique(list1):
    # initialize a null list
    uniqueList = []     
    # traverse for all elements
    for x in list1:
        # check if exists in uniqueList or not
        if x not in uniqueList:
            uniqueList.append(x)
    return len(uniqueList)

# Function to find the mean of the list
def mean (lst):
    return sum(lst) / len(lst)

# Function to find the median of the list
def Median(lst):
    listLength = len(lst)
    #lst.sort()
    temp = lst #bubble_sort(lst)
    if listLength % 2 == 0:
        median1 = temp[listLength//2]
        median2 = temp[listLength//2 - 1]
        median = (median1 + median2)/2
        return median
    else:
        median = temp[listLength//2]
        return median

# Function to find the mode of the list
def mode(data):
    frequency={}
    for number in data:
        frequency.setdefault(number,0)
        frequency[number]+=1
    highestFreq = max(frequency.values())
    highestFreqLst=[]
    for number, freq in frequency.items():
        if freq == highestFreq:
            highestFreqLst.append(number)
    return highestFreq

# Function to find percentiles of the data
def percentile(data, perc: int):
    #temp = list(data)
    size = len(data)
    #bubble_sort(data)
    return sorted(data)[int(math.ceil((size * perc) / 100)) - 1]

# Function to find the standardDeviation of the data
def standardD(data):
    Average = mean(data)   # mean
    vari  = sum(pow(x-Average,2) for x in data) / len(data)  # variance
    std  = math.sqrt(vari)  # standard deviation
    return std

# Function to find variance of the list
def variance(lst):
    avg = mean(lst)
    vari = sum((x-avg)**2 for x in lst) / len(lst)
    return vari

# Function to check for minimum number
def minNum(x):
  min_val = x[0] 
  for check in x: 
    if check < min_val: 
      min_val = check 
  return min_val

# Function to check for maximum number
def maxNum(x):
  max_val = x[0] 
  for check in x: 
    if check > max_val: 
      max_val = check 
  return max_val

#driver function
def most(lst):
    data = collections.Counter(lst)
    data_list = dict(data)
    max_value = max(list(data.values()))
    mode_val = [num for num, freq in data_list.items() if freq == max_value]
    if len(mode_val) == len(lst):
        return 0
    else:
        return mode_val
    
#finds the max length of rows
rowMax = 0
for row in rows:
    if(rowMax < len(row)):
        rowMax = len(row)
        
#deletes rows that doesnt have all the data
data = []
for row in rows:
    if(len(row) == rowMax):
        data.append(row)

#check to make sure that all lists are the same size
if len(set(map(len, data))) not in (0, 1):
    raise ValueError('not all lists have same length!')       


#transposes the matrix so columns and rows are flipped
transMatrix = zip(*data)
searchT_matrix = zip(*data)


####################Search function#######################
print("--Input q to quit the search function--")
userinput = 0
while userinput != 'q':
    print("--------------Search Function-------------------")
    userinput = input("Please enter Number to search for: ")
    userinputC = input("Please enter The column number you would like to search in: ")
    searchT_matrix = zip(*data)
    if(userinput != 'q'):
        rowNumber = 0
        presentNumber = 0
        try:
            for column in searchT_matrix:
                for row in column:
                    if(row == float(userinput)):
                        presentNumber +=1
                        print(f'\t {userinput} is present in column: {userinputC} row: {rowNumber}.')    
            rowNumber += 1
            print("-----------------------------------------------------------------")
            print(f'\t {userinput} is present {presentNumber} times in column: {userinputC}.')
        except:
            print("---The Inputs must be numerical Data---")
################################################################
    
count = []
uniq = []
Average = []
medi = []
mode = []
standardDev = []
vari = []
Percentile20 = []
Percentile40 = []
Percentile50 = []
Percentile60 = []
Percentile80 = []
mini = []
maxi = []
for row in transMatrix:
    #Merge_Sort the row before calculations 
    temp = []
    temp = merge_sort(row)

    count.append(len(temp))
    uniq.append(unique(temp))
    Average.append(mean(temp))
    medi.append(Median(temp))
    mode.append(statistics.mode(row))
    standardDev.append(standardD(row))
    vari.append(variance(temp))
    Percentile20.append(percentile(temp,20))
    Percentile40.append(percentile(temp,40))
    Percentile50.append(percentile(temp,50))
    Percentile60.append(percentile(temp,60))
    Percentile80.append(percentile(temp,80))
    mini.append(minNum(temp))
    maxi.append(maxNum(temp))
print("Descriptor     [Column A, Column B]")
print("**     **")
print("Count         ", count) 
print("Unique        ", uniq)
print("Mean          ", Average)
print("Median        ", medi)
print("Mode          ", mode)
print("SD            ", standardDev)
print("Variance      ", vari)
print("P20           ", Percentile20)
print("P40           ", Percentile40)
print("P50           ", Percentile50)
print("P60           ", Percentile60)
print("P80           ", Percentile80)
print("Minimum       ", mini)
print("Maximum       ", maxi)