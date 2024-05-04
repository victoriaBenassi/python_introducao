'''
   Algoritmo Bubble Sort
'''

lista =[60,40,29,1,2,4,5,8,9,11,3,90]

def bubble_sort(arr):

    n = len(arr)
    #Para cada elemento i do array
    for i in range(n):
        #Para cada elemento j do array
        for j in range(0, n-i-1):
            #Se elemento i for maior que elemento j 
            if arr[j] > arr[j+1]:
                #troca os elementos i e j
                arr[j], arr[j+1] = arr[j+1],arr[j] 
    return arr

print(bubble_sort(lista))