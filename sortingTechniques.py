list = [4,2,3,6,1,5,2]

# Selection Sort
def selection_sort(list):
    for i in range(len(list)-1):
        min = i
        for j in range(i,len(list)):
            if list[j] < list[min]:
                min = j
            
        temp = list[i]
        list[i] = list[min]
        list[min] = temp

    print(list)

#insertion Sort
def insertion_sort(list):
    for i in range(1,len(list)):
        j = i
        while list[j-1] > list[i] and j> 0:
            list[j-1], list[j] = list[j],list[j-1]
            j -= 1
            
    print(list)

# bubble sort
def bubble_sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

    print(list)


selection_sort(list)
insertion_sort(list)
bubble_sort(list)
