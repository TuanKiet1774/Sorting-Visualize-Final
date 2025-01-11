import time

###############################-SẮP XẾP CHỌN-###############################
def selection_sort(data, drawData, timeTick, ascending=True, pause_flag=None):
    for i in range(len(data)-1):
        idx = i
        for j in range(i+1, len(data)):
            if (ascending and data[j] < data[idx]) or (not ascending and data[j] > data[idx]):
                idx = j
            if pause_flag:
                pause_flag.wait()
        
        if idx != i:
            data[i], data[idx] = data[idx], data[i]
            drawData(data, ['green' if x == i or x == idx else 'red' for x in range(len(data))])
            time.sleep(timeTick)
            if pause_flag:
                pause_flag.wait()
    
    drawData(data, ['green' for x in range(len(data))])

###############################-SẮP XẾP CHÈN-###############################
def insertion_sort(data, drawData, timeTick, ascending=True, pause_flag=None):
    for i in range(1, len(data)):
        current_value = data[i]
        j = i - 1
        while j >= 0 and ((ascending and data[j] > current_value) or (not ascending and data[j] < current_value)):
            data[j + 1] = data[j]
            j -= 1
            if pause_flag:
                pause_flag.wait()
        data[j + 1] = current_value
        drawData(data, ['green' if x == j + 1 else 'red' for x in range(len(data))])
        time.sleep(timeTick)
        if pause_flag:
            pause_flag.wait()
    
    drawData(data, ['green' for x in range(len(data))])

###############################-SẮP XẾP NỔI BỌT-###############################
def bubble_sort(data, drawData, timeTick, ascending=True, pause_flag=None):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if (ascending and data[j] > data[j+1]) or (not ascending and data[j] < data[j+1]):
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))])
                time.sleep(timeTick)
                if pause_flag:
                    pause_flag.wait()
    
    drawData(data, ['green' for x in range(len(data))])

###############################-SẮP XẾP TRỘN-###############################
def merge_sort(data, drawData, timeTick, ascending=True, pause_flag=None):
    merge_sort_alg(data, 0, len(data)-1, drawData, timeTick, ascending, pause_flag)

def merge_sort_alg(data, left, right, drawData, timeTick, ascending, pause_flag):
    if left < right:
        middle = (left + right) // 2
        merge_sort_alg(data, left, middle, drawData, timeTick, ascending, pause_flag)
        merge_sort_alg(data, middle+1, right, drawData, timeTick, ascending, pause_flag)
        merge(data, left, middle, right, drawData, timeTick, ascending, pause_flag)

def merge(data, left, middle, right, drawData, timeTick, ascending, pause_flag):
    if pause_flag:
        pause_flag.wait()
    drawData(data, getColorArray_merge(len(data), left, middle, right))
    time.sleep(timeTick)
    
    leftPart = data[left:middle+1]
    rightPart = data[middle+1:right+1]
    leftIdx, rightIdx = 0, 0
    
    for dataIdx in range(left, right+1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if (ascending and leftPart[leftIdx] <= rightPart[rightIdx]) or (not ascending and leftPart[leftIdx] >= rightPart[rightIdx]):
                data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1
        elif leftIdx < len(leftPart):
            data[dataIdx] = leftPart[leftIdx]
            leftIdx += 1
        else:
            data[dataIdx] = rightPart[rightIdx]
            rightIdx += 1
        
        if pause_flag:
            pause_flag.wait()
        drawData(data, ["green" if x >= left and x <= right else "white" for x in range(len(data))])
        time.sleep(timeTick)

def getColorArray_merge(length, left, middle, right):
    colorArray = []

    for i in range(length):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append("yellow")
            else:
                colorArray.append("pink")
        else:
            colorArray.append("white")

    return colorArray

###############################-SẮP XẾP NHANH-###############################
def quick_sort(data, head, tail, drawData, timeTick, ascending, pause_flag=None):
    if head < tail:
        partitionIdx = partition(data, head, tail, drawData, timeTick, ascending, pause_flag)
        quick_sort(data, head, partitionIdx-1, drawData, timeTick, ascending, pause_flag)
        quick_sort(data, partitionIdx+1, tail, drawData, timeTick, ascending, pause_flag)

def partition(data, head, tail, drawData, timeTick, ascending, pause_flag):
    border = head
    pivot = data[tail]
    drawData(data, getColorArray_quick(len(data), head, tail, border, border))
    time.sleep(timeTick)

    for j in range(head, tail):
        if pause_flag:
            pause_flag.wait()
        if (ascending and data[j] < pivot) or (not ascending and data[j] > pivot):
            drawData(data, getColorArray_quick(len(data), head, tail, border, j, True))
            time.sleep(timeTick)
            if pause_flag:
                pause_flag.wait()
            data[border], data[j] = data[j], data[border]
            border += 1

    data[border], data[tail] = data[tail], data[border]
    return border

def getColorArray_quick(dataLen, head, tail, border, currIdx, isSwaping=False):
    colorArray = []
    for i in range(dataLen):
        # Base coloring
        if i >= head and i <= tail:
            colorArray.append('gray')
        else:
            colorArray.append('white')

        if i == tail:
            colorArray[i] = 'blue'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currIdx:
            colorArray[i] = 'yellow'

        if isSwaping:
            if i == border or i == currIdx:
                colorArray[i] = 'green'

    return colorArray

###############################-SẮP XẾP VUN ĐỐNG-###############################
def heapify(data, n, i, drawData, timeTick, ascending=True, pause_flag=None):
    largest_or_smallest = i
    left, right = 2*i + 1, 2*i + 2
    if left < n and ((ascending and data[left] > data[largest_or_smallest]) or (not ascending and data[left] < data[largest_or_smallest])):
        largest_or_smallest = left
    if right < n and ((ascending and data[right] > data[largest_or_smallest]) or (not ascending and data[right] < data[largest_or_smallest])):
        largest_or_smallest = right
    if largest_or_smallest != i:
        data[i], data[largest_or_smallest] = data[largest_or_smallest], data[i]
        drawData(data, ['green' if x == i or x == largest_or_smallest else 'red' for x in range(len(data))])
        time.sleep(timeTick)
        if pause_flag:
            pause_flag.wait()
        heapify(data, n, largest_or_smallest, drawData, timeTick, ascending, pause_flag)

def heap_sort(data, drawData, timeTick, ascending=True, pause_flag=None):
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i, drawData, timeTick, ascending, pause_flag)
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        drawData(data, ['green' if x == i else 'red' for x in range(len(data))])
        time.sleep(timeTick)
        if pause_flag:
            pause_flag.wait()
        heapify(data, i, 0, drawData, timeTick, ascending, pause_flag)
    drawData(data, ['green' for x in range(len(data))])
