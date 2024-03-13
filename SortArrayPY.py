"""
    simple demonstration of how to sort a list
"""

#sort using the selection sort algorithm
def select_sort(arr):   #takes one parameter: an array
    for i in range(len(arr)):		#iterate through each element of the array
        for j in range(len(arr)):	#at the same time, iterate within each iteration
            if (arr[i] < arr[j]):	#swap elements if the first is smaller than the second
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    
#sort using the bubble sort algorithm
def bubble_sort(arr):   #takes one parameter: an array
    sorted = False      #first, create a bool that will determine if we're going to loop
    while sorted == False:  #if we're not sorted yet, keep trying
        sorted = True       #this will remain true and break the loop if we properly sorted everything
        for i in range(len(arr)-1): #if we're not sorted yet, go through each element in the list and check the next value over
            if (arr[i] > arr[i+1]): #if the value we're at is less than the next value over...
                temp = arr[i]       #perform a swap between the current element and the next element over
                arr[i] = arr[i+1]
                arr[i+1] = temp
                sorted = False      #we had to perform a swap, so we'll have to repeat again



#create two lists
arr1 = [45, 52, 3, 86, 40]
arr2 = [87, 22, 41, 9, 5]

#print out our arrays as a demonstration before we sort
print("These are our arrays before sorting: ")
print("Array 1: ")
for i in range(len(arr1)):
    print(arr1[i])
print("Array 2: ")
for i in range(len(arr2)):
    print(arr2[i])

#test both of our sort algorithms to see if they work properly
print("Sort using selection sort: ")
select_sort(arr1)
for i in range(len(arr1)):
    print(arr1[i])

print("Sort using bubble sort: ")
bubble_sort(arr2)
for i in range(len(arr2)):
    print(arr2[i])

print('Program complete, have a nice day!')
