"""
input: 
arr: An array that is going to be sorted
output:
The input array but is sorted in ascending order
"""
def merge(arr):
    # If the length of the array is greater than 1 split the array into two slices
    if len(arr) > 1:
        mid = int(len(arr) / 2)  
        ls = arr[:mid]  # Create the left slice
        rs = arr[mid:]  # Create the right slice
        
        # Recursive call to merge to order each slice of the array
        merge(ls)
        merge(rs)
        
        # Initialize index for the left, right, and merged arrays
        i = 0
        j = 0
        k = 0
        
        #Mix left and right slices comparing his elements
        while i < len(ls) and j < len(rs):
            if ls[i] < rs[j]:  
                arr[k] = ls[i]
                i += 1
            else:  
                arr[k] = rs[j]
                j += 1
            k += 1  
        
        #add the remaining elements of the left array
        while i < len(ls):
            arr[k] = ls[i]
            i += 1
            k += 1
        
        #add the remaining elements of the right array
        while j < len(rs):
            arr[k] = rs[j]
            j += 1
            k += 1
    return arr
