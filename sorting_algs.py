import time
import random




#Bubble Sort

def bubble_sort(data, drawData, timeTick):
    for _ in range(len(data) - 1):
        for j in range(len(data)-1):
            if data[j] > data[j + 1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ["green" if x == j or x == j +1 else "red" for x in range(len(data))])
                time.sleep(timeTick)

    drawData(data, ["green" for x in range(len(data))])

#0(n**2) - quadratic 


#Quick sort

def partition(data, head, tail, drawData, timeTick):
    border = head
    pivot = data[tail]


    drawData(data, getCollorArray(len(data), head, tail, border, border))
    time.sleep(timeTick)
     
    for j in range(head, tail):
        if data[j] < pivot:
            drawData(data, getCollorArray(len(data), head, tail, border, j , True))
            time.sleep(timeTick)

            data[border], data[j] = data[j], data[border]
            border += 1
        
        drawData(data, getCollorArray(len(data), head, tail, border, j))
        time.sleep(timeTick)


    #Swap the pivot with border value

    drawData(data, getCollorArray(len(data), head, tail, border, tail, True))
    time.sleep(timeTick)

    data[border], data[tail] = data[tail], data[border]

    return border


def quick_sort(data, head, tail, drawData, timeTick):
    if head < tail:
        partition_Index = partition(data, head, tail, drawData, timeTick)

        #Left Partition
        quick_sort(data, head, partition_Index -1, drawData, timeTick)

        #Right Partition
        quick_sort(data, partition_Index +1, tail, drawData, timeTick)
"""
data = [10, 20, 4, 23, 77, 45]
quick_sort(data, 0, len(data)-1, 0, 0)
print(data)"""

def getCollorArray(dataLen, head, tail, border, curr_Index, is_swapping = False):
    colorArray = []
    for i in range(dataLen):
        #base coloring
        if i >= head and i <= tail:
            colorArray.append('gray')
        else:
            colorArray.append('white')
        if i == tail:
            colorArray[i] = 'blue'
        elif i == border:
            colorArray[i] = 'red'
        elif i == curr_Index:
            colorArray[i] = 'yellow'
        
        if is_swapping:
            if i == border or i == curr_Index:
                colorArray[i] = 'green'

    return colorArray




#Merge Sort.
def merge_sort_alg(data, left, right, drawData, timeTick):
    if left < right:
        middle = (left + right)//2
        merge_sort_alg(data, left, middle, drawData, timeTick)
        merge_sort_alg(data, middle+1, right, drawData, timeTick)
        merge(data, left, middle, right, drawData, timeTick)

def merge(data, left, middle, right, drawData, timetick):
    drawData(data, getColorArray(len(data), left, middle, right))
    time.sleep(timetick)


    left_part = data[left: middle + 1]
    right_part = data[middle + 1: right + 1]

    left_Index = right_Index = 0

    for data_index in range(left, right + 1):
        if left_Index < len(left_part) and right_Index < len(right_part):
            if left_part[left_Index] <= right_part[right_Index]:
                data[data_index] = left_part[left_Index]
                left_Index += 1
            else:
                data[data_index] = right_part[right_Index]
                right_Index += 1
            
        elif left_Index < len(left_part):
            data[data_index] = left_part[left_Index]
            left_Index += 1
        else:
            data[data_index] = right_part[right_Index]
            right_Index += 1

    drawData(data, ['green' if x>= left and x <= right else 'white' for x in range(len(data))])
    time.sleep(timetick)

def merge_sort(data, drawData, timeTick):
    merge_sort_alg(data, 0, len(data) - 1, drawData, timeTick)


"""data = [6, 2, 78, 34, 111, 17]
merge_sort(data, 0, 0)
print(data)"""

def getColorArray(length, left, middle, right):
    colorArray = []

    for i in range(length):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append("orange")
            else:
                colorArray.append("pink")
        else:
            colorArray.append('red')

    return colorArray



#Selection sort

def selection_sort(data, drawData, timeTick):
    for i in range(len(data)):
        minVal = data[i]
        min_index = i

        drawData(data, ["green" if x == i else "red" for x in range(len(data))])
        time.sleep(timeTick)
        

        for j in range(i +1, len(data)):

            drawData(data, ['green' if x == j else 'red' for x in range(len(data))])
            time.sleep(timeTick)

            if data[min_index] > data[j]:
                min_index = j
                minVal = data[j]

                drawData(data, ['yellow' if x == j else 'red' for x in range(len(data))])
                time.sleep(timeTick)

        #swap the minimum element with first element
        data[i], data[min_index] = data[min_index], data[i]

        drawData(data, ['green' if x == j else 'red' for x in range(len(data))])
        time.sleep(timeTick)



         