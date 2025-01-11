from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import threading
from Sort import *

root = Tk()
root.title('Mô phỏng thuật toán sắp xếp')
root.maxsize(900, 600)
root.config(bg='black')

# Variables
selected_alg = StringVar(value="Chọn thuật toán")  # Giá trị mặc định
data = []
sort_order = StringVar(value="Ascending")  # Giá trị mặc định cho sắp xếp

pause_flag = threading.Event()
pause_flag.set()  # Bắt đầu ở trạng thái chạy

def toggle_pause(event=None):
    if pause_flag.is_set():
        pause_flag.clear()  # Tạm dừng
    else:
        pause_flag.set()  # Tiếp tục

while not pause_flag.is_set():
    root.update_idletasks()  # Cho phép giao diện tiếp tục hoạt động


# Functions
def Display(data, colorArray):
    canvas.delete("all")
    c_height = 370
    c_width = 800
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    root.update_idletasks()

def Create_Array():
    global data
    min = int(minEntry.get())
    max = int(maxEntry.get())
    size = int(sizeEntry.get())
    data = [random.randrange(min, max+1) for _ in range(size)]
    Display(data, ['blue' for _ in range(len(data))])

def Sort_Algorithm():
    if selected_alg.get() == "Chọn thuật toán":
        messagebox.showwarning("Cảnh báo", "Hãy chọn một thuật toán!")
        return

    ascending = sort_order.get() == "Ascending"
    alg = selected_alg.get()

    # Định nghĩa hàm chạy thuật toán sắp xếp trong một thread
    def run_sort_algorithm():
        if alg == 'Quick Sort':
            quick_sort(data, 0, len(data)-1, Display, speedScale.get(), ascending, pause_flag)
        elif alg == 'Bubble Sort':
            bubble_sort(data, Display, speedScale.get(), ascending, pause_flag)
        elif alg == 'Merge Sort':
            merge_sort(data, Display, speedScale.get(), ascending, pause_flag)
        elif alg == 'Selection Sort':
            selection_sort(data, Display, speedScale.get(), ascending, pause_flag)
        elif alg == 'Insertion Sort':
            insertion_sort(data, Display, speedScale.get(), ascending, pause_flag)
        elif alg == 'Heap Sort':
            heap_sort(data, Display, speedScale.get(), ascending, pause_flag)

        # Sau khi thuật toán hoàn thành, hiển thị mảng đã sắp xếp
        Display(data, ['green' for _ in range(len(data))])

    # Tạo một thread mới để chạy thuật toán
    sort_thread = threading.Thread(target=run_sort_algorithm)
    sort_thread.start()

def Input_Array():
    def confirmArray():
        global data
        input_text = inputEntry.get()
        # Chuyển đổi chuỗi nhập vào thành danh sách số nguyên
        data = list(map(int, input_text.split()))
        Display(data, ['blue' for _ in range(len(data))])
        inputWindow.destroy()
        
        if len(data) == 0:
            messagebox.showwarning("Cảnh báo", "Dữ liệu nhập vào không đúng")
        return
    
    # Tạo cửa sổ con
    inputWindow = Toplevel(root)
    inputWindow.title("Nhập Mảng")
    inputWindow.geometry("400x200")
    inputWindow.config(bg="white")

    Label(inputWindow, text="Nhập các phần tử của mảng (cách nhau bởi dấu cách):", bg="white").pack(pady=10)
    inputEntry = Entry(inputWindow, width=50)
    inputEntry.pack(pady=10)

    Button(inputWindow, text="Xác nhận", command=confirmArray, bg="green").pack(pady=10)

# UI Layout
UI_frame = Frame(root, width=800, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=800, height=400, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

# Row[0]
Label(UI_frame, text="Thuật toán: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)

algorithms = ['Bubble Sort', 'Quick Sort', 'Merge Sort', 'Selection Sort', 'Insertion Sort', 'Heap Sort']
OptionMenu(UI_frame, selected_alg, *algorithms).grid(row=0, column=1, padx=5, pady=5)

speedScale = Scale(UI_frame, from_=0.1, to=5.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Tốc độ")
speedScale.grid(row=0, column=2, padx=5, pady=5)

# Row[1]
sizeEntry = Scale(UI_frame, from_=5, to=30, resolution=1, orient=HORIZONTAL, label="Số lượng")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)
minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Giá trị nhỏ nhất")
minEntry.grid(row=1, column=1, padx=5, pady=5)
maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Giá trị lớn nhất")
maxEntry.grid(row=1, column=2, padx=5, pady=5)

# Row[2]
Label(UI_frame, text="Chiều: ", bg='grey').grid(row=2, column=0, padx=5, pady=5, sticky=W)
Radiobutton(UI_frame, text="Tăng dần", variable=sort_order, value="Ascending", bg='grey').grid(row=2, column=1, padx=5, pady=5)
Radiobutton(UI_frame, text="Giảm dần", variable=sort_order, value="Descending", bg='grey').grid(row=2, column=2, padx=5, pady=5)

# Row[3]
Button(UI_frame, text="Tạo mảng", command=Create_Array, bg='yellow').grid(row=3, column=0, padx=5, pady=5)
Button(UI_frame, text="Nhập Mảng", command=Input_Array, bg='blue').grid(row=3, column=1, padx=5, pady=5)
Button(UI_frame, text="Bắt đầu", command=Sort_Algorithm, bg='green').grid(row=3, column=2, padx=5, pady=5)

root.bind('<space>', toggle_pause)

root.mainloop()
