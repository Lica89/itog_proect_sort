

import tkinter as tk
import time

class Menu:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Sorting Program")                    # создаем глваное окно
        self.input_field = tk.Entry(self.window, width=40)      # создаем поле ввода
        self.input_field.pack(pady=10)                          # добавляем на окно
        self.sort_options = tk.StringVar(self.window)
        self.sort_options.set("Selection Sort")                 # значение по умолчанию
        # создаем список для выбора метода сортировки
        self.sort_dropdown = tk.OptionMenu(self.window, self.sort_options, "Selection Sort", "Bubble Sort",
                                           "Merge Sort", "Heap Sort", "Counting Sort")
        self.sort_dropdown.pack()
        self.sort_button = tk.Button(self.window, text="Start", command=self.sort_numbers)
        self.sort_button.pack(pady=10)                          # добавляем на окно
        self.output_field = tk.Text(self.window, height=5, width=40)
        self.output_field.pack(pady=10)
        self.results_field = tk.Text(self.window, height=15, width=40)
        self.results_field.pack(pady=10)
        self.results = []  # Список для хранения результатов сортировки
        self.run()

    def run(self):
        # запускаем главный цикл приложения
        self.window.mainloop()

    def sort_numbers(self):

        try:
            # получаем мeтодои get() введенную последовательность чисел
            input_text = self.input_field.get()
            # преобразем строку в список,разделяем Split запятыми  пробраз кажд элем в float число
            nums = [float(num) for num in input_text.split(",")]
            # создаем объект класса Sort
            sorter = Sort()
            selected_sort = self.sort_options.get()
            # выбираем метод сортировки в зависимости от выбранного варианта в списке
            if selected_sort == "Selection Sort":
                start_time = time.time()
                sorted_nums = sorter.selection_sort(nums)
                elapsed_time = time.time() - start_time
                self.results.append(("Selection Sort", sorted_nums, elapsed_time))
            elif selected_sort == "Bubble Sort":
                start_time = time.time()
                sorted_nums = sorter.bubble_sort(nums)
                elapsed_time = time.time() - start_time
                self.results.append(("Bubble Sort", sorted_nums, elapsed_time))
            elif selected_sort == "Merge Sort":
                start_time = time.time()
                sorted_nums = sorter.merge_sort(nums)
                elapsed_time = time.time() - start_time
                self.results.append(("Merge Sort", sorted_nums, elapsed_time))
            elif selected_sort == "Heap Sort":
                start_time = time.time()
                sorted_nums = sorter.heap_sort(nums)
                elapsed_time = time.time() - start_time
                self.results.append(("Heap Sort", sorted_nums, elapsed_time))
            elif selected_sort == "Counting Sort":
                start_time = time.time()
                sorted_nums = sorter.counting_sort(nums)
                elapsed_time = time.time() - start_time
                self.results.append(("Counting Sort", sorted_nums, elapsed_time))

            self.output_field.delete("1.0", tk.END)
            self.output_field.insert(tk.END, str(self.results[-1][1]))  # Отображение последнего результата сортировки

            self.results_field.delete("1.0", tk.END)
            for result in self.results:
                sort_name = result[0]
                time_taken = result[2]
                self.results_field.insert(tk.END, f"Sort Name: {sort_name}\n")
                self.results_field.insert(tk.END, f"Time taken: {time_taken} seconds\n\n")
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid input. Please enter a comma-separated list of numbers.")

from sort import Sort

menu = Menu()
menu.run()




# import tkinter as tk
# import time
#
# # главное меню программы
# class Menu:
#     def __init__(self):
#         self.window = tk.Tk()
#         self.window.title("Sorting Program") # создаем глваное окно
#         self.input_field = tk.Entry(self.window, width=40) # создаем поле ввода
#         self.input_field.pack(pady=10) # добавляем на окно
#         self.sort_options = tk.StringVar(self.window)
#         self.sort_options.set("Selection Sort") # значение по умолчанию
#         # создаем список для выбора метода сортировки
#         self.sort_dropdown = tk.OptionMenu(self.window, self.sort_options, "Selection Sort", "Bubble Sort",
#                                            "Merge Sort", "Heap Sort", "Counting Sort")
#         self.sort_dropdown.pack() # добавляем на окно
#         self.sort_button = tk.Button(self.window, text="Start", command=self.sort_numbers) # метод sort_numbers вызывается при нажатии Start
#         self.sort_button.pack(pady=10) # добавляем на окно
#         self.output_field = tk.Text(self.window, height=5, width=40)
#         self.output_field.pack(pady=10)
#         self.time_field = tk.Text(self.window, height=1, width=40)
#         self.time_field.pack(pady=10)
#         self.run()
#
#     def run(self):
#         self.window.mainloop()
#
#     def sort_numbers(self):
#         global sorted_nums, end_time
#         try:
#             input_text = self.input_field.get() # получаем мнтодои get() введенную последовательность чисел
#             nums = [int(num) for num in input_text.split(",")] # преобразем строку в список,разделяем Split запятыми т пробраз кажд элем в целое число
#             sorter = Sort() # создаем объект класса Sort
#             selected_sort = self.sort_options.get()
#             if selected_sort == "Selection Sort":
#                 start_time = time.time()
#                 sorted_nums = sorter.selection_sort(nums)
#                 end_time = time.time()
#             elif selected_sort == "Bubble Sort":
#                 start_time = time.time()
#                 sorted_nums = sorter.bubble_sort(nums)
#                 end_time = time.time()
#             elif selected_sort == "Merge Sort":
#                 start_time = time.time()
#                 sorted_nums = sorter.merge_sort(nums)
#                 end_time = time.time()
#             elif selected_sort == "Heap Sort":
#                 start_time = time.time()
#                 sorted_nums = sorter.heap_sort(nums)
#                 end_time = time.time()
#             elif selected_sort == "Counting Sort":
#                 start_time = time.time()
#                 sorted_nums = sorter.counting_sort(nums)
#                 end_time = time.time()
#             self.output_field.delete("1.0", tk.END)
#             self.output_field.insert(tk.END, str(sorted_nums))
#             self.time_field.delete("1.0", tk.END)
#             self.time_field.insert(tk.END, "Time taken: {:.5f} seconds".format(end_time - start_time))
#         except ValueError:
#             tk.messagebox.showerror("Error", "Invalid input. Please enter a comma-separated list of integers.")
#
# #  класс Sort определяет методы сортировок
# class Sort:
#     @staticmethod
#     def bubble_sort(nums):
#         # Реализация пузырьковой сортировки
#         n = len(nums)
#         for i in range(n):
#             for j in range(0, n-i-1):
#                     if nums[j] > nums[j+1]:
#                         nums[j], nums[j+1] = nums[j+1], nums[j]
#         return nums
#     @staticmethod
#     def selection_sort(nums):
#         # Реализация сортировки выбором
#         pass
#
#     @staticmethod
#     def merge_sort(nums):
#         # Реализация сортировки слиянием
#         pass
#
#     @staticmethod
#     def heap_sort(nums):
#         # Реализация пирамидальной сортировки
#         pass
#
#     @staticmethod
#     def counting_sort(nums):
#         # Реализация сортировки подсчетом
#         pass
#
#
# menu = Menu()
# menu.run()







# import tkinter as tk
# import time
#
# class Menu:
#     def init(self):
#         self.window = tk.Tk()
#         self.window.title("Sorting Program")
#         # создаем поле ввода для последовательности чисел
#         self.input_field = tk.Entry(self.window, width=40)
#         self.input_field.pack(pady=10)
#         # создаем раскрывающийся список для выбора метода сортировки
#         self.sort_options = tk.StringVar(self.window)
#         self.sort_options.set("Selection Sort")
#         self.sort_dropdown = tk.OptionMenu(self.window, self.sort_options, "Selection Sort", "Bubble Sort")
#         self.sort_dropdown.pack()
#
#         # создаем кнопку для запуска сортировки
#         self.sort_button = tk.Button(self.window, text="Start", command=self.sort_numbers)
#         self.sort_button.pack(pady=10)
#
#         # создаем текстовое поле вывода для отсортированной последовательности чисел
#         self.output_field = tk.Text(self.window, height=5, width=40)
#         self.output_field.pack(pady=10)
#
#         # создаем текстовое поле вывода для времени затраченного на сортировку
#         self.time_field = tk.Text(self.window, height=1, width=40)
#         self.time_field.pack(pady=10)
#         self.run()
#
#     def run(self):
#         # запускаем главный цикл приложения
#         self.window.mainloop()
#
#     def sort_numbers(self):
#         try:
#             # получаем введенную пользователем последовательность чисел
#             input_text = self.input_field.get()
#             # преобразуем строку в список чисел
#             nums = [int(num) for num in input_text.split(",")]
#             # создаем объект класса Sort
#             sorter = Sort()
#             # выбираем метод сортировки в зависимости от выбранного варианта в списке
#             selected_sort = self.sort_options.get()
#             if selected_sort == "Selection Sort":
#                 start_time = time.time()
#                 sorted_nums = self.selection_sort(nums)
#                 end_time = time.time()
#             elif selected_sort == "Bubble Sort":
#                 start_time = time.time()
#                 sorted_nums = self.bubble_sort(nums)
#                 end_time = time.time()
#             # выводим отсортированный список в текстовое поле вывода
#             self.output_field.delete("1.0", tk.END)
#             self.output_field.insert(tk.END, str(sorted_nums))
#             # выводим время затраченное на сортировку
#             self.time_field.delete("1.0", tk.END)
#             self.time_field.insert(tk.END, "Time taken: {:.5f} seconds".format(end_time - start_time))
#         except ValueError:
#             tk.messagebox.showerror("Error", "Invalid input. Please enter a comma-separated list of integers.")
#
#     # функция сортировки выбором
#     def selection_sort(self, nums):
#         for i in range(len(nums)):
#             min_idx = i
#             for j in range(i+1, len(nums)):
#                 if nums[j] < nums[min_idx]:
#                     min_idx = j
#             nums[i], nums[min_idx] = nums[min_idx], nums[i]
#         return nums
#
#     # функция сортировки пузырьком
#     def bubble_sort(self, nums):
#         n = len(nums)
#         for i in range(n):
#             for j in range(0, n-i-1):
#                 if nums[j] > nums[j+1]:
#                     nums[j], nums[j+1] = nums[j+1], nums[j]
#         return nums
# class Sort:
#     # функция сортировки пирамидальным методом
#     @staticmethod
#     def heap_sort(nums):
#         def heapify(nums, n, i):
#             largest = i
#             l = 2 * i + 1
#             r = 2 * i + 2
#             if l < n and nums[i] < nums[l]:
#                 largest = l
#             if r < n and nums[largest] < nums[r]:
#                 largest = r
#             if largest != i:
#                 nums[i], nums[largest] = nums[largest], nums[i]
#                 heapify(nums, n, largest)
#         n = len(nums)
#         for i in range(n // 2 - 1, -1, -1):
#             heapify(nums, n, i)
#         for i in range(n - 1, 0, -1):
#             nums[i], nums[0] = nums[0], nums[i]
#             heapify(nums, i, 0)
#         return nums
#     # функция сортировки слиянием
#     @staticmethod
#     def merge_sort(nums):
#         if len(nums) > 1:
#             mid = len(nums) // 2
#             left_half = nums[:mid]
#             right_half = nums[mid:]
#             Sort.merge_sort(left_half)
#             Sort.merge_sort(right_half)
#             i = j = k = 0
#             while i < len(left_half) and j < len(right_half):
#                 if left_half[i] < right_half[j]:
#                     nums[k] = left_half[i]
#                     i += 1
#                 else:
#                     nums[k] = right_half[j]
#                     j += 1
#                 k += 1
#             while i < len(left_half):
#                 nums[k] = left_half[i]
#                 i += 1
#                 k += 1
#             while j < len(right_half):
#                 nums[k] = right_half[j]
#                 j += 1
#                 k += 1
#         return nums
#
#     # функция бинарного поиска
#     @staticmethod
#     def binary_search(nums, target):
#         low = 0
#         high = len(nums) - 1
#         while low <= high:
#             mid = (low + high) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         return -1
#
#     # функция сортировки подсчетом
#     @staticmethod
#     def counting_sort(nums):
#         max_num = max(nums)
#         count = [0] * (max_num + 1)
#         for num in nums:
#             count[num] += 1
#         sorted_nums = []
#         for i in range(len(count)):
#             for j in range(count[i]):
#                 sorted_nums.append(i)
#         return sorted_nums
#     #функция сортировки  selection_sort
#     @staticmethod
#     def selection_sort(nums):
#         for i in range(len(nums)):
#             min_index = i
#             for j in range(i + 1, len(nums)):
#                 if nums[j] < nums[min_index]:
#                     min_index = j
#             nums[i], nums[min_index] = nums[min_index], nums[i]
#         return nums
#     # функция пузырквой сортировки
#     @staticmethod
#     def bubble_sort(nums):
#         n = len(nums)
#         for i in range(n):
#             for j in range(0, n - i - 1):
#                 if nums[j] > nums[j + 1]:
#                     nums[j], nums[j + 1] = nums[j + 1], nums[j]
#         return nums
#
#     # функция сортировки insertion
#     @staticmethod
#     def insertion_sort(nums):
#         for i in range(1, len(nums)):
#             key = nums[i]
#             j = i - 1
#             while j >= 0 and key < nums[j]:
#                 nums[j + 1] = nums[j]
#                 j -= 1
#             nums[j + 1] = key
#         return nums
# menu = Menu()
# menu.run()
