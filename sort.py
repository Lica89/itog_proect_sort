class Sort:
    @staticmethod

    def bubble_sort(nums):
        """
        сортировка пузырьком
        :param nums: список чисел для сортировки
        :return: отсортированный список
        """
        n = len(nums)                   # Получаем длину списка чисел
        for i in range(n - 1):          # внешний цикл-проходим по всем элементам списка, кроме последнего
            for j in range(n - 1 - i):  # внутренний цикл- проходим по непоследним элементам каждой итерации
                if nums[j] > nums[j+1]: # Если текущий элемент больше следующего
                    nums[j], nums[j+1] = nums[j+1], nums[j] # Меняем местами элементы
        return nums

    @staticmethod # counting_sort

    def counting_sort(nums):
        """
        сортировка подсчтетом
        :param nums: список чисел для сортировки
        :return: отсортированный список
        """
        count = {}          # Создаем пустой словарь для подсчета чисел
        for num in nums:
            if num in count:
                count[num] += 1 # если число уже есть -увеличиваем счетчик для этого числа на 1
            else:
                count[num] = 1  # Если нет числа -добавляем число в словарь со значением 1

        sorted_nums = []    # пустой список для отсортированных чисел
        for num in sorted(count.keys()): # Обходим отсортированные ключи словаря
            sorted_nums.extend([num] * count[num]) # Добавляем число в список count раз

        return sorted_nums
    @staticmethod
    def merge_sort(nums):
        """
        сортировка слиянием
        :param nums: Список чисел, который нужно отсортировать.
        :return: Отсортированный список чисел.
        """
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2    # целосичленное деление для определнения середины списка
        left_half = nums[:mid]  # срез списка от начала до mid(без элемента с mid)
        right_half = nums[mid:] # срез списка от mid(с элементом с mid) до конца списка

        left_half = Sort.merge_sort(left_half) #рекурсивно выполняется merge_sort для каждого среза.
        right_half = Sort.merge_sort(right_half)

        return Sort.merge(left_half, right_half) #оортированные половины сливаются вместе
    @staticmethod
    def merge(left_half, right_half):
        """
        Функция, которая выполняет слияние двух отсортированных списков.
        :param left_half:Отсортированный список чисел.
        :param right_half:Отсортированный список чисел.
        :return:Отсортированный список чисел.
        """
        merged = []
        left_index, right_index = 0, 0

        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] <= right_half[right_index]:
                merged.append(left_half[left_index])
                left_index += 1
            else:
                merged.append(right_half[right_index])
                right_index += 1

        while left_index < len(left_half):
            merged.append(left_half[left_index])
            left_index += 1

        while right_index < len(right_half):
            merged.append(right_half[right_index])
            right_index += 1

        return merged

    @staticmethod
    def heapify(nums, n, i):
        """
        Функция, которая выполняет преобразование поддерева в кучу (heapify).
        :param nums: список чисел, для которого нужно выполнить heapify
        :param n: количество элементов в списке
        :param i: индекс элемента, с которого нужно начать heapify
        :return: None
        """
        largest = i         # переменная, которая инициализируется индексом корня поддерева.
        left = 2 * i + 1    # переменная, которая содержит индекс левого потомка
        right = 2 * i + 2   # переменная, которая содержит индекс правого потомка

        if left < n and nums[i] < nums[left]:
            largest = left

        if right < n and nums[largest] < nums[right]:
            largest = right

        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            Sort.heapify(nums, n, largest)

    @staticmethod
    def heap_sort(nums):
        """
        Функция, которая выполняет сортировку списка с использованием пирамидальной сортировки (heap sort).

        :param nums: Список чисел
        :return: Отсортированный список чисел
        """
        n = len(nums)

        for i in range(n // 2 - 1, -1, -1):
            Sort.heapify(nums, n, i)

        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            Sort.heapify(nums, i, 0)

        return nums

    @staticmethod # selection_sort
    def selection_sort(nums):
        """
        Функция, которая выполняет сортировку списка с использованием сортировки выбором (selection sort)
        :param nums:Список чисел
        :return:Отсортированный список чисел
        """

        n = len(nums)      # переменная длины списка `nums`
        for i in range(n): # внешний цикл
            min_index = i  # ищем наименьший элемент в оставшемся списке
            for j in range(i+1, n):
                if nums[j] < nums[min_index]: # Обмен наименьшего значения с текущим элементом
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums

