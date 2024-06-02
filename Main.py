import random

def fill_array_with_random_values(size, min_value=0, max_value=100):
    """
    Функция заполняет массив случайными значениями.
    
    :param size: Размер массива
    :param min_value: Минимальное значение случайного числа (включительно)
    :param max_value: Максимальное значение случайного числа (включительно)
    :return: Массив, заполненный случайными значениями
    """
    array = [random.randint(min_value, max_value) for _ in range(size)]
    return array

def print_array(array):
    """
    Функция выводит массив на экран.
    
    :param array: Массив для вывода
    """
    for element in array:
        print(element)

# Пример использования функций

if __name__ == "__main__":
    size = 10  # Размер массива
    min_value = 1  # Минимальное значение случайного числа
    max_value = 50  # Максимальное значение случайного числа
    
    random_array = fill_array_with_random_values(size, min_value, max_value)
    print("Сгенерированный массив случайных значений:")
    print_array(random_array)
