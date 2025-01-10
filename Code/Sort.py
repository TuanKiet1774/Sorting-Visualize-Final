import time

###############################-SẮP XẾP CHỌN-###############################
def selection_sort(data, drawData, timeTick, ascending = True):
    for i in range(len(data)-1):
        idx = i  # Giả sử phần tử cần tìm là phần tử đầu tiên chưa được sắp xếp
        for j in range(i+1, len(data)):
            # Nếu sắp xếp theo chiều tăng dần
            if (ascending and data[j] < data[idx]) or (not ascending and data[j] > data[idx]):
                idx = j  # Cập nhật chỉ số phần tử cần tìm

        # Hoán đổi nếu phần tử cần tìm không phải là phần tử ban đầu
        if idx != i:
            data[i], data[idx] = data[idx], data[i]
            drawData(data, ['green' if x == i or x == idx else 'red' for x in range(len(data))])
            time.sleep(timeTick)

    # Hiển thị màu xanh cho toàn bộ mảng sau khi sắp xếp xong
    drawData(data, ['green' for x in range(len(data))])
    
###############################-SẮP XẾP CHÈN-###############################
def insertion_sort(data, drawData, timeTick, ascending=True):
    for i in range(1, len(data)):
        current_value = data[i]
        j = i - 1    
        # sang một vị trí bên phải để chừa chỗ cho current_value
        while j >= 0 and ((ascending and data[j] > current_value) or (not ascending and data[j] < current_value)):
            data[j + 1] = data[j]
            j -= 1
        
        # Chèn giá trị hiện tại vào đúng vị trí
        data[j + 1] = current_value
        
        # Cập nhật đồ họa cho mỗi lần chèn
        drawData(data, ['green' if x == j + 1 else 'red' for x in range(len(data))])
        time.sleep(timeTick)
    
    # Hiển thị màu xanh cho toàn bộ mảng sau khi sắp xếp xong
    drawData(data, ['green' for x in range(len(data))])

###############################-SẮP XẾP NỔI BỌT-###############################
def bubble_sort(data, drawData, timeTick, ascending=True):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            # Thay đổi điều kiện so sánh tùy thuộc vào hướng sắp xếp
            if (ascending and data[j] > data[j+1]) or (not ascending and data[j] < data[j+1]):
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))])
                time.sleep(timeTick)
    drawData(data, ['green' for x in range(len(data))])

###############################-SẮP XẾP TRỘN-###############################
def merge_sort(data, drawData, timeTick, ascending=True):
    merge_sort_alg(data, 0, len(data)-1, drawData, timeTick, ascending)

def merge_sort_alg(data, left, right, drawData, timeTick, ascending):
    if left < right:
        middle = (left + right) // 2
        merge_sort_alg(data, left, middle, drawData, timeTick, ascending)
        merge_sort_alg(data, middle+1, right, drawData, timeTick, ascending)
        merge(data, left, middle, right, drawData, timeTick, ascending)

def merge(data, left, middle, right, drawData, timeTick, ascending):
    drawData(data, getColorArray(len(data), left, middle, right))
    time.sleep(timeTick)

    leftPart = data[left:middle+1]
    rightPart = data[middle+1: right+1]

    leftIdx = rightIdx = 0

    for dataIdx in range(left, right+1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            # Điều kiện so sánh thay đổi tùy theo chiều sắp xếp
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
    
    drawData(data, ["green" if x >= left and x <= right else "white" for x in range(len(data))])
    time.sleep(timeTick)

def getColorArray(length, left, middle, right):
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
def partition(data, head, tail, drawData, timeTick, ascending = True):
    border = head
    pivot = data[tail]

    drawData(data, getColorArray(len(data), head, tail, border, border))
    time.sleep(timeTick)

    for j in range(head, tail):
        # Điều chỉnh điều kiện so sánh theo chiều sắp xếp
        if (ascending and data[j] < pivot) or (not ascending and data[j] > pivot):
            drawData(data, getColorArray(len(data), head, tail, border, j, True))
            time.sleep(timeTick)

            data[border], data[j] = data[j], data[border]
            border += 1

        drawData(data, getColorArray(len(data), head, tail, border, j))
        time.sleep(timeTick)

    # Swap pivot with border value
    drawData(data, getColorArray(len(data), head, tail, border, tail, True))
    time.sleep(timeTick)

    data[border], data[tail] = data[tail], data[border]
    
    return border

def quick_sort(data, head, tail, drawData, timeTick, ascending):
    if head < tail:
        partitionIdx = partition(data, head, tail, drawData, timeTick, ascending)

        # LEFT PARTITION
        quick_sort(data, head, partitionIdx-1, drawData, timeTick, ascending)

        # RIGHT PARTITION
        quick_sort(data, partitionIdx+1, tail, drawData, timeTick, ascending)

def getColorArray(dataLen, head, tail, border, currIdx, isSwaping=False):
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
def heapify(data, n, i, drawData, timeTick, ascending=True):
    largest_or_smallest = i  # Gốc hiện tại
    left = 2 * i + 1  # Con trái
    right = 2 * i + 2  # Con phải

    # Nếu con trái lớn hơn (hoặc nhỏ hơn nếu sắp xếp giảm dần) gốc
    if left < n and ((ascending and data[left] > data[largest_or_smallest]) or 
                     (not ascending and data[left] < data[largest_or_smallest])):
        largest_or_smallest = left

    # Nếu con phải lớn hơn (hoặc nhỏ hơn nếu sắp xếp giảm dần) gốc
    if right < n and ((ascending and data[right] > data[largest_or_smallest]) or 
                      (not ascending and data[right] < data[largest_or_smallest])):
        largest_or_smallest = right

    # Nếu gốc không phải là lớn nhất (hoặc nhỏ nhất)
    if largest_or_smallest != i:
        data[i], data[largest_or_smallest] = data[largest_or_smallest], data[i]
        drawData(data, ['green' if x == i or x == largest_or_smallest else 'red' for x in range(len(data))])
        time.sleep(timeTick)

        # Đệ quy heapify cây con bị thay đổi
        heapify(data, n, largest_or_smallest, drawData, timeTick, ascending)

def heap_sort(data, drawData, timeTick, ascending=True):
    n = len(data)

    # Xây dựng một max heap hoặc min heap (tùy thuộc vào thứ tự sắp xếp)
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i, drawData, timeTick, ascending)

    # Trích xuất từng phần tử khỏi heap
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]  # Hoán đổi phần tử gốc với phần tử cuối
        drawData(data, ['green' if x == i else 'red' for x in range(len(data))])
        time.sleep(timeTick)

        # Gọi heapify trên heap đã giảm kích thước
        heapify(data, i, 0, drawData, timeTick, ascending)

    # Hiển thị màu xanh cho toàn bộ mảng sau khi sắp xếp xong
    drawData(data, ['green' for x in range(len(data))])
