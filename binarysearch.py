
def binarySearch(array,key,low,high):
	if high >= low:
		mid = low + (high - low)//2
        	if array[mid] == key:
            		return mid
        	elif array[mid] > key:
            		return binarySearch(array, key, low, mid-1)
        	else:
           		 return binarySearch(array, key, high, mid+1)
	else:
        	return -1


array = [3, 4, 5, 6, 7, 8, 9]
key = 6
result = binarySearch(array, key, 0, len(array)-1)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
