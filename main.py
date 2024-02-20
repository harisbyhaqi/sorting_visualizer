import tkinter as tk
import random
import time

class SortingVisualizer:
    def __init__(self, master):
        self.master = master
        self.master.title("Sorting Visualizer")

        self.array_size = tk.IntVar(value=10)
        self.array = []

        self.create_buttons()

    def create_buttons(self):
        self.canvas = tk.Canvas(self.master, height=300, width=600, bg="white")
        self.canvas.pack(pady=10)

        self.size_label = tk.Label(self.master, text="Array Size:")
        self.size_label.pack()

        self.size_scale = tk.Scale(self.master, from_=5, to=30, orient=tk.HORIZONTAL, variable=self.array_size, command=self.generate_array)
        self.size_scale.pack()

        self.shuffle_button = tk.Button(self.master, text="Shuffle", command=self.shuffle_array)
        self.shuffle_button.pack()

        self.sort_button = tk.Button(self.master, text="Start Sorting", command=self.start_sorting)
        self.sort_button.pack()

        self.stop_button = tk.Button(self.master, text="Stop Sorting", command=self.stop_sorting, state=tk.DISABLED)
        self.stop_button.pack()

        self.sorting_algorithm = tk.StringVar(value="Bubble Sort")
        self.algorithm_menu = tk.OptionMenu(self.master, self.sorting_algorithm, "Bubble Sort", "Quick Sort", "Merge Sort", "Insertion Sort")
        self.algorithm_menu.pack()

    def generate_array(self, *args):
        self.array = random.sample(range(1, 100), self.array_size.get())
        self.draw_array()

    def draw_array(self):
        self.canvas.delete("all")
        bar_width = 600 / len(self.array)
        for i, height in enumerate(self.array):
            x0, y0 = i * bar_width, 300 - height
            x1, y1 = (i + 1) * bar_width, 300
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="blue")

    def shuffle_array(self):
        random.shuffle(self.array)
        self.draw_array()

    def start_sorting(self):
        self.sort_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        algorithm = self.sorting_algorithm.get()
        if algorithm == "Bubble Sort":
            self.bubble_sort()
        elif algorithm == "Quick Sort":
            self.quick_sort(self.array, 0, len(self.array) - 1)
        elif algorithm == "Merge Sort":
            self.merge_sort(self.array)
        elif algorithm == "Insertion Sort":
            self.insertion_sort()

        self.sort_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def stop_sorting(self):
        self.sort_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def bubble_sort(self):
        n = len(self.array)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    self.draw_array()
                    self.master.update()
                    time.sleep(0.1)

    def quick_sort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                self.draw_array()
                self.master.update()
                time.sleep(0.1)
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        self.draw_array()
        self.master.update()
        time.sleep(0.1)
        return i + 1

    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

            self.draw_array()
            self.master.update()
            time.sleep(0.1)

    def insertion_sort(self):
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i - 1
            while j >= 0 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
                self.draw_array()
                self.master.update()
                time.sleep(0.1)
            self.array[j + 1] = key
            self.draw_array()
            self.master.update()
            time.sleep(0.1)

if __name__ == "__main__":
    root = tk.Tk()
    app = SortingVisualizer(root)
    root.mainloop()
