

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




#