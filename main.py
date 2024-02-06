arr = [2,3,6,4,5,1]

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n-1):

        for j in range(0,n-i-1):

            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

bubble_sort(arr)
print(arr)

def selection_sort(arr):
    for i in range(len(arr)):
        smallest = i
        for j in range(i+1,len(arr)):
            if arr[smallest] < arr[j]:
                smallest = j
    arr[i],arr[smallest] = arr[smallest],arr[i]

selection_sort(arr)
print(arr)