# Задача №1: Загрузка на github через git bash.

Переход в указанный каталог

![image](https://github.com/KnyazevaAM/PMIIS/assets/70960325/8b4436c5-92be-498f-81c1-7b2a7e0bda31)

Добавление файлов в индекс для отслеживания изменений и проверка

![image](https://github.com/KnyazevaAM/PMIIS/assets/70960325/f87825a8-9a0b-4ddc-8660-8a2ec5694290)

Запушим в git

![image](https://github.com/KnyazevaAM/PMIIS/assets/70960325/9cd8e2f5-b716-4c6b-b292-4587a97540f7)

Создание тега

![image](https://github.com/KnyazevaAM/PMIIS/assets/70960325/96424bb5-13b5-479f-a5a7-b76a8ff54969)


# Описание кода Задание №2 Вариант №14

12.	Напишите две функции. Первая функция заполняет массив случайными значениями, вторая функция выводит массив на экран
```
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
```

# Пример вывода

![image](https://github.com/KnyazevaAM/PMIIS/assets/70960325/29882265-c111-4bab-bb82-76154b83f11e)

# Описание кода Задание №3 Вариант №14

8.	Вывод виде таблицы ФИО и среднеарифметическую оценку по всем предметам по зачетке
import pandas as pd

# Данные по зачеткам

```
zachetki = [
    {
        'ФИО': 'Иванов Иван Иванович',
        'Математика': 4,
        'Физика': 5,
        'Химия': 3
    },
    {
        'ФИО': 'Петров Петр Петрович',
        'Математика': 5,
        'Физика': 4,
        'Химия': 5
    },
    {
        'ФИО': 'Сидоров Сидор Сидорович',
        'Математика': 3,
        'Физика': 3,
        'Химия': 4
    }
]

# Создаем DataFrame из списка словарей
df = pd.DataFrame(zachetki)

# Вычисляем среднеарифметическую оценку по всем предметам для каждого студента
df['Средний балл'] = df.iloc[:, 1:].mean(axis=1)

# Выводим таблицу с ФИО и среднеарифметической оценкой
result = df[['ФИО', 'Средний балл']]
print(result)
```

![image](https://github.com/KnyazevaAM/PMIIS/assets/70960325/2fe8ab37-2ab4-476d-ad9f-ef625b45c559)

